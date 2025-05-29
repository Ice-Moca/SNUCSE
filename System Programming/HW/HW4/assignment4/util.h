/*---------------------------------------------------------------------------*/
/* util.h                                                                    */
/* Author: Jongki Park, Kyoungsoo Park                                       */
/*---------------------------------------------------------------------------*/

#ifndef _UTIL_H_
#define _UTIL_H_

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <errno.h>

#include "token.h"
#include "dynarray.h"

enum {FALSE, TRUE};

enum BuiltinType {NORMAL, B_EXIT, B_CD};
enum PrintMode {SETUP, PERROR, FPRINTF};

void error_print(char *input, enum PrintMode mode);
enum BuiltinType check_builtin(struct Token *t);
int count_pipe(DynArray_T oTokens);
int check_bg(DynArray_T oTokens);
void dump_lex(DynArray_T oTokens);

#endif /* _UTIL_H_ */