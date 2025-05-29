/*---------------------------------------------------------------------------*/
/* execute.c                                                                 */
/* Author: Jongki Park, Kyoungsoo Park                                       */
/*---------------------------------------------------------------------------*/

#include "dynarray.h"
#include "token.h"
#include "util.h"
#include "lexsyn.h"
#include "snush.h"
#include "execute.h"
#include "job.h"

// extern struct job_manager *manager;
/*---------------------------------------------------------------------------*/
void redout_handler(char *fname) {
	//
	// TODO: redout_handler() in execute.c
	//
	// fd is used to open the file for output redirection.
	int fd = open(fname, O_WRONLY | O_CREAT | O_TRUNC, 0640);
	// if the file descriptor is less than 0, it indicates an error occurred while opening the file.
	// else, it duplicates the file descriptor to STDOUT_FILENO, effectively redirecting standard output to the file.
    if (fd < 0) {
        error_print(NULL, PERROR);
        exit(EXIT_FAILURE);
    } 
	else {
        dup2(fd, STDOUT_FILENO);
        close(fd);
    } 
	//
	// TODO: redout_handler() in execute.c
	// 
}
/*---------------------------------------------------------------------------*/
void redin_handler(char *fname) {
	int fd;

	fd = open(fname, O_RDONLY);
	if (fd < 0) {
		error_print(NULL, PERROR);
		exit(EXIT_FAILURE);
	}
	else {
		dup2(fd, STDIN_FILENO);
		close(fd);
	}
}
/*---------------------------------------------------------------------------*/
int build_command_partial(DynArray_T oTokens, int start, 
						int end, char *args[]) {
	int i, ret = 0, redin = FALSE, redout = FALSE, cnt = 0;
	struct Token *t;

	/* Build command */
	for (i = start; i < end; i++) {

		t = dynarray_get(oTokens, i);

		if (t->token_type == TOKEN_WORD) {
			if (redin == TRUE) {
				redin_handler(t->token_value);
				redin = FALSE;
			}
			else if (redout == TRUE) {
				redout_handler(t->token_value);
				redout = FALSE;
			}
			else
				args[cnt++] = t->token_value;
		}
		else if (t->token_type == TOKEN_REDIN)
			redin = TRUE;
		else if (t->token_type == TOKEN_REDOUT)
			redout = TRUE;
	}
	args[cnt] = NULL;

#ifdef DEBUG
	for (i = 0; i < cnt; i++)
	{
		if (args[i] == NULL)
			printf("CMD: NULL\n");
		else
			printf("CMD: %s\n", args[i]);
	}
	printf("END\n");
#endif
	return ret;
}
/*---------------------------------------------------------------------------*/
int build_command(DynArray_T oTokens, char *args[]) {
	return build_command_partial(oTokens, 0, 
								dynarray_get_length(oTokens), args);
}
/*---------------------------------------------------------------------------*/
void execute_builtin(DynArray_T oTokens, enum BuiltinType btype) {
	int ret;
	char *dir = NULL;
	struct Token *t1;

	switch (btype) {
	case B_EXIT:
		if (dynarray_get_length(oTokens) == 1) {
			// printf("\n");
			dynarray_map(oTokens, free_token, NULL);
			dynarray_free(oTokens);

			exit(EXIT_SUCCESS);
		}
		else
			error_print("exit does not take any parameters", FPRINTF);

		break;

	case B_CD:
		if (dynarray_get_length(oTokens) == 1) {
			dir = getenv("HOME");
			if (dir == NULL) {
				error_print("cd: HOME variable not set", FPRINTF);
				break;
			}
		}
		else if (dynarray_get_length(oTokens) == 2) {
			t1 = dynarray_get(oTokens, 1);
			if (t1->token_type == TOKEN_WORD)
				dir = t1->token_value;
		}

		if (dir == NULL) {
			error_print("cd takes one parameter", FPRINTF);
			break;
		}
		else {
			ret = chdir(dir);
			if (ret < 0)
				error_print(NULL, PERROR);
		}
		break;

	default:
		error_print("Bug found in execute_builtin", FPRINTF);
		exit(EXIT_FAILURE);
	}
}
/*---------------------------------------------------------------------------*/
void wait_fg(int jobid) {
	while (1) {
        struct job *job = find_job_by_jid(jobid);

        if (job == NULL) {
            break;
        }

        if (job->state != foreground) {
            break;
        }
        sleep(0);
    }

    return;
}
/*---------------------------------------------------------------------------*/
void print_job(int jobid, pid_t pgid) {
    fprintf(stdout, 
		"[%d] Process group: %d running in the background\n", jobid, pgid);
}
/*---------------------------------------------------------------------------*/
int fork_exec(DynArray_T oTokens, int is_background) {
	//
	// TODO-START: fork_exec() in execute.c
	//
	// 1. Add a new job and get its job id.
	pid_t pid;
    char *args[MAX_ARGS_CNT];
    int jobid = add_job(oTokens, is_background ? background : foreground);

	// 2. Fork a new process.
    pid = fork();

	// 2-1. Handle fork failure.
    if (pid < 0) {
        error_print("fork failed", PERROR);
        return -1;
    }
	// 2-2. Child process logic.
    else if (pid == 0) {
		// (child) Set its own process group.
		setpgid(0, 0);
        // (child) Build the command arguments (redirection is handled inside build_command).
		build_command(oTokens, args);
        // (child) Execute the command. If exec fails, print error and exit.
        if (execvp(args[0], args) < 0) {
            error_print(args[0], PERROR);
            exit(EXIT_FAILURE);
        }
    } 
    // 2-3. Parent process logic.
	else {
        // (parent) Set the child's process group.
        setpgid(pid, pid);
        // (parent) Register the child's PID to the job.
        register_pid_to_job(jobid, pid);
        // (parent) If it's the first process in the job, set the job's PGID.
        struct job *job = find_job_by_jid(jobid);
        if (job) job->pgid = pid;
        // 3. Wait for foreground jobs or print info for background jobs.
        if (!is_background) {
            // (parent) Foreground: wait until job finishes.
            wait_fg(jobid);
        } 
		// If the job is in the background, it prints the job information.
		else {
            // (parent) Background: print job info, do not wait.
            print_job(jobid, pid);
        }
    }
    // 4. Return the job id.
    return jobid;
	//
	// TODO-END: fork_exec() in execute.c
	//
}
/*---------------------------------------------------------------------------*/
int iter_pipe_fork_exec(int n_pipe, DynArray_T oTokens, int is_background) {
	//
	// TODO-START: iter_pipe_fork_exec() in execute.c
	//
	// 1. Add a new job and get its job id.
	int pipe_fd[2], prev_fd = -1, start = 0, end, pipe_idx = 0;
    pid_t pid;
    char *args[MAX_ARGS_CNT];
    int jobid = add_job(oTokens, is_background ? background : foreground);

    // 2. For each segment (between pipes), fork a new process.
    struct job *job = find_job_by_jid(jobid);
    for (int i = 0; i <= dynarray_get_length(oTokens); i++) {
        struct Token *t = (i < dynarray_get_length(oTokens)) ? dynarray_get(oTokens, i) : NULL;
        // If it's a pipe or the end of the token array, handle this segment.
        if (t == NULL || t->token_type == TOKEN_PIPE) {
            end = i;
			// 2-1. Create a pipe if needed.
            if (pipe_idx < n_pipe) {
                pipe(pipe_fd);
            }
            // 2-2. Fork the process.
            pid = fork();
            // 2-2-1. Handle fork failure.
            if (pid < 0) {
                error_print("fork failed", PERROR);
                return -1;
            }
            // 2-2-2. Child process logic.
            else if (pid == 0) { 
                // (child) Set the process group for the job.
                setpgid(0, jobid);
                // (child) If there is a previous pipe, set stdin to it.
                if (prev_fd != -1) {
                    dup2(prev_fd, STDIN_FILENO);
                    close(prev_fd);
                }
                // (child) If not the last segment, set stdout to the pipe.
                if (pipe_idx < n_pipe) {
                    dup2(pipe_fd[1], STDOUT_FILENO);
                    close(pipe_fd[0]);
                    close(pipe_fd[1]);
                }
                // (child) Build and execute the command for this segment.
                build_command_partial(oTokens, start, end, args);
                execvp(args[0], args);
                error_print(args[0], PERROR);
                exit(EXIT_FAILURE);
            } 
            // 2-2-3. Parent process logic.
			else {
                // (parent) Set the child's process group.
                setpgid(pid, jobid);
                // (parent) Register the child's PID to the job.
                register_pid_to_job(jobid, pid);
                // (parent) For the first process, set the job's PGID.
                if (job && pipe_idx == 0) job->pgid = pid;
                // (parent) Close the previous pipe read end.
                if (prev_fd != -1) close(prev_fd);
                // (parent) For next segment, set prev_fd to current pipe's read end.
                if (pipe_idx < n_pipe) {
                    close(pipe_fd[1]);
                    prev_fd = pipe_fd[0];
                }
                // Update segment index and start position for the next command.
                pipe_idx++;
                start = end + 1;
            }
        }
    }
    // 3. Foreground: wait until all processes finish. Background: print job info.
    if (!is_background) {
        wait_fg(jobid);
    } 
	else {
        print_job(jobid, job->pgid);
    }
    // 4. Return the job id.
    return jobid;
	//
	// TODO-END: iter_pipe_fork_exec() in execute.c
	//
}
/*---------------------------------------------------------------------------*/