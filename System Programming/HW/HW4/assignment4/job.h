/*---------------------------------------------------------------------------*/
/* job.h                                                                     */
/* Author: Jongki Park, Kyoungsoo Park, EunSu Yeo                            */
/*---------------------------------------------------------------------------*/

#ifndef _JOB_H_
#define _JOB_H_

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <assert.h>

#include "dynarray.h"  
#include "token.h"     

#define MAX_JOBS 16

typedef enum State {
    unknown = 0,
    foreground,
    background,
    stopped,
} job_state;

/* 
 * Job = The user's command line input
 * ex) if the user's command line input is "ps -ef | grep job" then 
 * One job, Two processes. 
 */
struct job {
    int job_id;
    job_state state;
    pid_t pgid;
    pid_t *pid_list;
    int total_num;
    int curr_num;
    struct job *next;
};

/* 
 * One global variable for a job manager. 
 * When a job is created, register it with the job manager, 
 * regardless of whether it is a foreground or background job.
 * When the background job is finished, add it in the done_bg_jobs.
 */
struct job_manager {
    int n_jobs;
    struct job *jobs;
    struct job *done_bg_jobs;
};

void init_job_manager();
struct job *find_job_by_jid(int job_id);
struct job *find_job_fg();

//
// TODO: new job control functions in job.h start
// 
void register_pid_to_job(int job_id, pid_t pid);
int add_job(DynArray_T oTokens, job_state state);
void remove_pid_from_job(int job_id, pid_t pid);
void move_job_to_done_bg(int job_id);
//
// TODO: new job control functions in job.h end
// 

#endif /* _JOB_H_ */