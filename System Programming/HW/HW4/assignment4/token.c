/*---------------------------------------------------------------------------*/
/* token.c                                                                   */
/* Author: Jongki Park, Kyoungsoo Park                                       */
/*---------------------------------------------------------------------------*/

#include "token.h"

/*---------------------------------------------------------------------------*/
struct Token *make_one_token(enum TokenType token_type, char *token_value) {
    struct Token *new_token;

    new_token = (struct Token *)malloc(sizeof(struct Token));
    if (new_token == NULL)
        return NULL;

    new_token->token_type = token_type;

    if (token_value != NULL) {
        /* \0 exists at the end of the token_value */
        new_token->token_value = (char *)malloc(strlen(token_value) + 1);
        if (new_token->token_value == NULL) {
            free(new_token);
            return NULL;
        }

        strcpy(new_token->token_value, token_value);
    }
    else
        new_token->token_value = NULL;

    return new_token;
}
/*---------------------------------------------------------------------------*/
void free_token(void *v_item, void *v_extra) {
    struct Token *psToken = (struct Token *)v_item;

    if (psToken->token_value != NULL)
        free(psToken->token_value);

    free(psToken);
}
/*---------------------------------------------------------------------------*/