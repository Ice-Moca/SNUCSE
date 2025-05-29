/*---------------------------------------------------------------------------*/
/* token.h                                                                   */
/* Author: Jongki Park, Kyoungsoo Park                                       */
/*---------------------------------------------------------------------------*/

#ifndef _TOKEN_H_
#define _TOKEN_H_

#include <stdlib.h>
#include <string.h>

enum TokenType {
  TOKEN_PIPE,
  TOKEN_REDIN,
  TOKEN_REDOUT,
  TOKEN_WORD,
  TOKEN_BG
};

struct Token {
  /* The type of the token. */
  enum TokenType token_type;

  /* The string which is the token's value. */
  char *token_value;
};

/* Create and return a Token whose type is token_type and whose
       value consists of string token_value.  Return NULL if insufficient
       memory is available.  The caller owns the Token. */
struct Token *make_one_token(enum TokenType token_type, char *token_value);


/* Free token v_item.  v_extra is unused. */
void free_token(void *v_item, void *v_extra);

#endif /* _TOKEN_H_ */