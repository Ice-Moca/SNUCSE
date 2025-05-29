/*---------------------------------------------------------------------------*/
/* lexsyn.h                                                                  */
/* Author: Jongki Park, Kyoungsoo Park                                       */
/*---------------------------------------------------------------------------*/

#ifndef _LEXSYN_H
#define _LEXSYN_H

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#include "dynarray.h"

enum {MAX_LINE_SIZE = 1024};
enum {MAX_ARGS_CNT = 64};

enum LexResult {LEX_SUCCESS, LEX_QERROR, LEX_NOMEM, LEX_LONG};
enum SyntaxResult {
  SYN_SUCCESS,
  SYN_FAIL_NOCMD,
  SYN_FAIL_MULTREDIN, 
  SYN_FAIL_NODESTIN,
  SYN_FAIL_MULTREDOUT,
  SYN_FAIL_NODESTOUT,
  SYN_FAIL_INVALIDBG,
};

// void command_lexLine(const char * c_line, DynArray_T ctokens);
enum LexResult lexLine_quote(const char *c_line, DynArray_T oTokens);
enum LexResult lex_line(const char *c_line, DynArray_T oTokens);
enum SyntaxResult syntax_check(DynArray_T oTokens);

#endif /* _LEXSYN_H */