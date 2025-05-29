/*---------------------------------------------------------------------------*/
/* execute.h                                                                 */
/* Author: Jongki Park, Kyoungsoo Park                                       */
/*---------------------------------------------------------------------------*/

#ifndef _EXECUTE_H_
#define _EXECUTE_H_

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

void redout_handler(char *fname);
void redin_handler(char *fname);
int build_command_partial(DynArray_T oTokens, int start, 
                            int end, char *args[]);
int build_command(DynArray_T oTokens, char *args[]);
void execute_builtin(DynArray_T oTokens, enum BuiltinType btype);
void wait_fg(int jobid);
void print_job(int jobid, pid_t pgid);
int fork_exec(DynArray_T oTokens, int is_background);
int iter_pipe_fork_exec(int pCount, DynArray_T oTokens, int is_background);

#endif /* _EXEUCTE_H_ */