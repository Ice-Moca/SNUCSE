/*---------------------------------------------------------------------------*/
/* job.c                                                                     */
/* Author: Jongki Park, Kyoungsoo Park                                       */
/*---------------------------------------------------------------------------*/

#include "job.h"

extern struct job_manager *manager;
/*---------------------------------------------------------------------------*/
void init_job_manager() {
	manager = (struct job_manager *)calloc(1, sizeof(struct job_manager));
	if (manager == NULL) {
		fprintf(stderr, "[Error] job manager allocation failed\n");
		exit(EXIT_FAILURE);
	}
}
/*---------------------------------------------------------------------------*/
struct job *find_job_by_jid(int job_id) {
    if (manager == NULL) {
        fprintf(stderr, "[Error] find_job_by_jid: Job manager is NULL\n");
        return NULL;
    }

    struct job *current = manager->jobs;

    while (current != NULL) {
        if (current->job_id == job_id) {
            return current;
        }
        current = current->next;
    }

    return NULL;
}
/*---------------------------------------------------------------------------*/
struct job *find_job_fg() {
    if (manager == NULL) {
        fprintf(stderr, "[Error] find_job_fg: Job manager is NULL\n");
        return NULL;
    }

    struct job *current = manager->jobs;

    while (current != NULL) {
        if (current->state == foreground) {
            return current;
        }
        current = current->next;
    }

    return NULL;
}
/*---------------------------------------------------------------------------*/
//
// TODO: new job control functions in job.c start
// 
// Registers a new process PID into the job's PID list.
void register_pid_to_job(int job_id, pid_t pid) {
    // Find the job by job_id.
    struct job *job = find_job_by_jid(job_id);
    if (!job) return;
    // If there is still room, add the pid to the list.
    if (job->curr_num < job->total_num) {
        job->pid_list[job->curr_num++] = pid;
    }
}

// Creates a new job, assigns an available job ID (0 ~ MAX_JOBS-1), and initializes job metadata.
int add_job(DynArray_T oTokens, job_state state) {
    int i;
    // Allocate memory for the new job.
    struct job *new_job = (struct job *)calloc(1, sizeof(struct job));
    if (!new_job) return -1;
    // Find unused job_id (slot) between 0 and MAX_JOBS-1.
    int used[MAX_JOBS] = {0};
    struct job *cur = manager->jobs;
    // Mark all used job_ids from active jobs.
    while (cur) { used[cur->job_id] = 1; cur = cur->next; }
    // Also mark job_ids in the done_bg_jobs list.
    cur = manager->done_bg_jobs;
    while (cur) { used[cur->job_id] = 1; cur = cur->next; }
    // Find the first unused slot.
    for (i = 0; i < MAX_JOBS; ++i) {
        if (!used[i]) { new_job->job_id = i; break; }
    }
    if (i == MAX_JOBS) { free(new_job); return -1; } // No available slot

    // Set job state and PGID (process group id).
    new_job->state = state;
    new_job->pgid = 0;
    // Determine the number of processes by counting pipes.
    int n_processes = 1;
    for (int i = 0; i < dynarray_get_length(oTokens); i++) {
        struct Token *t = dynarray_get(oTokens, i);
        if (t->token_type == TOKEN_PIPE) n_processes++;
    }
    // Initialize process count and PID list.
    new_job->total_num = n_processes;
    new_job->curr_num = 0;
    new_job->pid_list = (pid_t *)calloc(n_processes, sizeof(pid_t));
    // Add to the head of the jobs linked list.
    new_job->next = manager->jobs;
    manager->jobs = new_job;
    manager->n_jobs++;
    // Return the allocated job_id.
    return new_job->job_id;
}

// Removes a PID from the job's PID list, and cleans up the job if no processes remain.
void remove_pid_from_job(int job_id, pid_t pid) {
    // Find the job.
    struct job *job = find_job_by_jid(job_id);
    if (!job) return;
    int i;
    // Find the PID in the list and remove it (shift left).
    for (i = 0; i < job->curr_num; ++i) {
        if (job->pid_list[i] == pid) {
            for (int j = i + 1; j < job->curr_num; ++j)
                job->pid_list[j - 1] = job->pid_list[j];
            job->curr_num--;
            break;
        }
    }
    // If all PIDs are removed and it's a foreground job, free and remove the job.
    if (job->curr_num == 0 && job->state == foreground) {
        struct job **pp = &manager->jobs;
        while (*pp && (*pp)->job_id != job_id) pp = &(*pp)->next;
        if (*pp) {
            struct job *to_free = *pp;
            *pp = to_free->next;
            manager->n_jobs--;
            free(to_free->pid_list);
            free(to_free);
        }
    }
    // If all PIDs are removed and it's a background job, move to done_bg_jobs.
    else if (job->curr_num == 0 && job->state == background) {
        move_job_to_done_bg(job_id);
    }
}

// Moves a finished background job from the active job list to the done_bg_jobs list.
void move_job_to_done_bg(int job_id) {
    struct job **pp = &manager->jobs;
    struct job *job = NULL;
    // Find the job in the jobs list.
    while (*pp && (*pp)->job_id != job_id) pp = &(*pp)->next;
    if (*pp) {
        job = *pp;
        // Remove from the active job list.
        *pp = job->next;
        manager->n_jobs--;
        // Add to the head of the done_bg_jobs list.
        job->next = manager->done_bg_jobs;
        manager->done_bg_jobs = job;
    }
}
//
// TODO: new job control functions in job.c end
// 
/*---------------------------------------------------------------------------*/