/*---------------------------------------------------------------------------*/
/* lexsyn.h                                                                  */
/* Author: Jongki Park, Kyoungsoo Park                                       */
/*---------------------------------------------------------------------------*/

#include "lexsyn.h"
#include "token.h"
#include "util.h"

/*---------------------------------------------------------------------------*/
static int add_to_token_array(DynArray_T oTokens, 
                            enum TokenType type, char *value) {
    struct Token *new_token;

    new_token = make_one_token(type, value);
    if (new_token == NULL) {
        error_print("Cannot allocate memory", FPRINTF);
        return FALSE;
    }

    if (!dynarray_add(oTokens, new_token)) {
        error_print("Cannot allocate memory", FPRINTF);
        return FALSE;
    }

    return TRUE;
}
/*---------------------------------------------------------------------------*/
enum LexResult lex_line(const char *c_line, DynArray_T oTokens) {

    /* It "reads" its characters from c_line. */

    enum LexState {
        STATE_START,
        STATE_IN_WORD,
        STATE_IN_DQUOTE,
        STATE_IN_QUOTE
    };

    enum LexState state = STATE_START;

    int command_line_index = 0;
    int value_index = 0;
    char c;
    char c_value[MAX_LINE_SIZE];

    assert(c_line != NULL);
    assert(oTokens != NULL);

    for (;;) {
        if (command_line_index == MAX_LINE_SIZE)
            return LEX_LONG;
        
        /* "Read" the next character from c_line. */
        c = c_line[command_line_index++];

        switch (state) {
        case STATE_START:
            if ((c == '\n') || (c == '\0'))
                return LEX_SUCCESS;
            else if (isspace(c))
                state = STATE_START;
            else if (c == '|') {
                /* Create a PIPE token. */
                if (add_to_token_array(oTokens, TOKEN_PIPE, NULL) == FALSE)
                    return LEX_NOMEM;

                state = STATE_START;
            }
            else if (c == '&') {
                // Create a Background command token.
                if (add_to_token_array(oTokens, TOKEN_BG, NULL) == FALSE)
                    return LEX_NOMEM;

                state = STATE_START;
            }
            else if (c == '>') {
                /* Create a REDOUT token. */
                if (add_to_token_array(oTokens, TOKEN_REDOUT, NULL) == FALSE)
                    return LEX_NOMEM;

                state = STATE_START;
            }
            else if (c == '<') {
                /* Create a PIPE token. */
                if (add_to_token_array(oTokens, TOKEN_REDIN, NULL) == FALSE)
                    return LEX_NOMEM;

                state = STATE_START;
            }
            else if (c == '\"') {
                state = STATE_IN_DQUOTE;
            }
            else if (c == '\'') {
                state = STATE_IN_QUOTE;
            }
            else {
                c_value[value_index++] = c;
                state = STATE_IN_WORD;
            }
            break;

        case STATE_IN_WORD:
            if ((c == '\n') || (c == '\0')) {
                /* Create a WORD token. */
                c_value[value_index] = '\0';
                if (add_to_token_array(oTokens, TOKEN_WORD, c_value) == FALSE)
                    return LEX_NOMEM;

                value_index = 0;

                return LEX_SUCCESS;
            }
            else if (isspace(c)) {
                /* Create a WORD token. */
                c_value[value_index] = '\0';
                if (add_to_token_array(oTokens, TOKEN_WORD, c_value) == FALSE)
                    return LEX_NOMEM;

                value_index = 0;

                state = STATE_START;
            }
            else if (c == '|') {
                /* Create a WORD token. */
                c_value[value_index] = '\0';
                if (add_to_token_array(oTokens, TOKEN_WORD, c_value) == FALSE)
                    return LEX_NOMEM;

                /* Create a PIPE token. */
                if (add_to_token_array(oTokens, TOKEN_PIPE, NULL) == FALSE)
                    return LEX_NOMEM;

                value_index = 0;

                state = STATE_START;
            }
            else if (c == '>') {
                /* Create a WORD token. */
                c_value[value_index] = '\0';
                if (add_to_token_array(oTokens, TOKEN_WORD, c_value) == FALSE)
                    return LEX_NOMEM;

                /* Create a REDOUT token. */
                if (add_to_token_array(oTokens, TOKEN_REDOUT, NULL) == FALSE)
                    return LEX_NOMEM;

                value_index = 0;

                state = STATE_START;
            }
            else if (c == '<') {
                /* Create a WORD token. */
                c_value[value_index] = '\0';
                if (add_to_token_array(oTokens, TOKEN_WORD, c_value) == FALSE)
                    return LEX_NOMEM;

                /* Create a REDIN token. */
                if (add_to_token_array(oTokens, TOKEN_REDIN, NULL) == FALSE)
                    return LEX_NOMEM;

                value_index = 0;

                state = STATE_START;
            }
            else if (c == '&') {
                // Create a WORD token

                c_value[value_index] = '\0';
                if (add_to_token_array(oTokens, TOKEN_WORD, c_value) == FALSE)
                    return LEX_NOMEM;

                // Create a Background command token.
                if (add_to_token_array(oTokens, TOKEN_BG, NULL) == FALSE)
                    return LEX_NOMEM;

                value_index = 0;
                state = STATE_START;
            }
            else if (c == '\"') {
                state = STATE_IN_DQUOTE;
            }
            else if (c == '\'') {
                state = STATE_IN_QUOTE;
            }
            else {
                c_value[value_index++] = c;
                state = STATE_IN_WORD;
            }
            break;

        case STATE_IN_DQUOTE:
            if (c == '\"')
                state = STATE_IN_WORD;
            else if ((c == '\n') || (c == '\0'))
                return LEX_QERROR;
            else
                c_value[value_index++] = c;

            break;

        case STATE_IN_QUOTE:
            if (c == '\'')
                state = STATE_IN_WORD;
            else if ((c == '\n') || (c == '\0'))
                return LEX_QERROR;
            else
                c_value[value_index++] = c;
            break;

        default:
            assert(FALSE);
        }
    }
}
/*---------------------------------------------------------------------------*/
enum SyntaxResult syntax_check(DynArray_T oTokens) {
    int i;
    enum SyntaxResult ret = SYN_SUCCESS;
    int ri_exist = FALSE, ro_exist = FALSE, p_exist = FALSE;
    struct Token *t_curr, *t_next;

    assert(oTokens);

    for (i = 0; i < dynarray_get_length(oTokens); i++) {
        t_curr = dynarray_get(oTokens, i);
        if (i == 0) {
            if (t_curr->token_type != TOKEN_WORD) {
                /* Missing command name */
                ret = SYN_FAIL_NOCMD;
                break;
            }
        }
        else {
            if (t_curr->token_type == TOKEN_PIPE) {
                /* No redout in previous tokens and 
                    no consecutive pipe in following tokens */
                if (ro_exist == TRUE) {
                    /* Multiple redirection error */
                    ret = SYN_FAIL_MULTREDOUT;
                    break;
                }
                else {
                    if (i == dynarray_get_length(oTokens) - 1) {
                        /* Redirection without destination */
                        ret = SYN_FAIL_NOCMD;
                        break;
                    }
                    else {
                        t_next = dynarray_get(oTokens, i + 1);
                        if (t_next->token_type != TOKEN_WORD) {
                            /* Redirection without destination */
                            ret = SYN_FAIL_NOCMD;
                            break;
                        }
                    }
                    p_exist = TRUE;
                }
            }
            else if (t_curr->token_type == TOKEN_BG) {
                if (i != dynarray_get_length(oTokens) - 1) {
                    ret = SYN_FAIL_INVALIDBG;
                    break;
                }
            }
            else if (t_curr->token_type == TOKEN_REDIN) {
                /* No pipe in previous tokens and 
                    no redin in following tokens */
                if ((p_exist == TRUE) || (ri_exist == TRUE)) {
                    /* Multiple redirection error */
                    ret = SYN_FAIL_MULTREDIN;
                    break;
                }
                else {
                    if (i == dynarray_get_length(oTokens) - 1) {
                        /* Redirection without destination */
                        ret = SYN_FAIL_NODESTIN;
                        break;
                    }
                    else {
                        t_next = dynarray_get(oTokens, i + 1);
                        if (t_next->token_type != TOKEN_WORD) {
                            /* Redirection without destination */
                            ret = SYN_FAIL_NODESTIN;
                            break;
                        }
                    }
                    ri_exist = TRUE;
                }
            }
            else if (t_curr->token_type == TOKEN_REDOUT) {
                /* No redout in following tokens */
                if (ro_exist == TRUE) {
                    /* Multiple redirection error */
                    ret = SYN_FAIL_MULTREDOUT;
                    break;
                }
                else {
                    if (i == dynarray_get_length(oTokens) - 1) {
                        /* Redirection without destination */
                        ret = SYN_FAIL_NODESTOUT;
                        break;
                    }
                    else {
                        t_next = dynarray_get(oTokens, i + 1);
                        if (t_next->token_type != TOKEN_WORD) {
                            /* Redirection without destination */
                            ret = SYN_FAIL_NODESTOUT;
                            break;
                        }
                    }
                    ro_exist = TRUE;
                }
            }
        }
    }

    return ret;
}
/*---------------------------------------------------------------------------*/