/*---------------------------------------------------------------------------*/
/* util.c                                                                    */
/* Author: Jongki Park, Kyoungsoo Park                                       */
/*---------------------------------------------------------------------------*/

#include "util.h"

/*---------------------------------------------------------------------------*/
void error_print(char *input, enum PrintMode mode) {
    static char *ishname = NULL;

    if (mode == SETUP)
        ishname = input;
    else {
        if (ishname == NULL) {
            fprintf(stderr, "Initialization failed: Shell name not set\n");
            fflush(stderr);
            exit(EXIT_FAILURE);
        }
        else {
            if (mode == PERROR) {
                if (input == NULL)
                    fprintf(stderr, "%s: %s\n", ishname, strerror(errno));
                else
                    fprintf(stderr, "%s: %s\n", input, strerror(errno));
            }
            else if (mode == FPRINTF)
                fprintf(stderr, "%s: %s\n", ishname, input);
            else
                fprintf(stderr, "mode %d not supported "\
                        "in error_print\n", mode);

            fflush(stderr);
        }
    }
}
/*---------------------------------------------------------------------------*/
enum BuiltinType check_builtin(struct Token *t) {
    /* Check null input before using string functions  */
    assert(t);
    assert(t->token_value);

    if (strncmp(t->token_value, "cd", 2) == 0 && strlen(t->token_value) == 2)
        return B_CD;
    if (strncmp(t->token_value, "exit", 4) == 0 && strlen(t->token_value) == 4)
        return B_EXIT;
    else
        return NORMAL;
}
/*---------------------------------------------------------------------------*/
int count_pipe(DynArray_T oTokens) {
    int cnt = 0, i;
    struct Token *t;

    for (i = 0; i < dynarray_get_length(oTokens); i++) {
        t = dynarray_get(oTokens, i);
        if (t->token_type == TOKEN_PIPE)
            cnt++;
    }

    return cnt;
}
/*---------------------------------------------------------------------------*/
/* Check if the user demands it to run as background processes */
int check_bg(DynArray_T oTokens) {
    int i;
    struct Token *t;

    for (i = 0; i < dynarray_get_length(oTokens); i++) {
        t = dynarray_get(oTokens, i);
        if (t->token_type == TOKEN_BG)
            return 1;
    }
    return 0;
}
/*---------------------------------------------------------------------------*/
const char *special_token_to_str(struct Token *sp_token) {
    switch (sp_token->token_type)
    {
    case TOKEN_PIPE:
        return "TOKEN_PIPE(|)";
        break;
    case TOKEN_REDIN:
        return "TOKEN_REDIRECTION_IN(<)";
        break;
    case TOKEN_REDOUT:
        return "TOKEN_REDIRECTION_OUT(>)";
        break;
    case TOKEN_BG:
        return "TOKEN_BACKGROUND(&)";
        break;
    case TOKEN_WORD:
        /* This should not be called with TOKEN_WORD */
    default:
        assert(0 && "Unreachable");
        return NULL;
    }
}
/*---------------------------------------------------------------------------*/
void dump_lex(DynArray_T oTokens) {
    if (getenv("DEBUG") != NULL) {
        int i;
        struct Token *t;

        for (i = 0; i < dynarray_get_length(oTokens); i++) {
            t = dynarray_get(oTokens, i);
            if (t->token_value == NULL)
                fprintf(stderr, "[%d] %s\n", i, special_token_to_str(t));
            else
                fprintf(stderr, 
                            "[%d] TOKEN_WORD(\"%s\")\n", i, t->token_value);
        }
    }
}
/*---------------------------------------------------------------------------*/