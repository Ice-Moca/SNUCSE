/*---------------------------------------------------------------------------*/
/* skvslib.c                                                                 */
/* Author: Junghan Yoon, KyoungSoo Park                                      */
/*---------------------------------------------------------------------------*/
#include "skvslib.h"
/*---------------------------------------------------------------------------*/
/* response messages and commands */
const char *g_msgs[MSG_COUNT]
    = { "INVALID CMD", "CREATE OK", "COLLISION",   "NOT FOUND",
        "UPDATE OK",   "DELETE OK", "INTERNAL ERR" };
const char *g_cmds[CMD_COUNT] = { "CREATE", "READ", "UPDATE", "DELETE" };
const char *g_lf = "\n";
/*---------------------------------------------------------------------------*/
static inline enum CMD
skvs_parse (char *buffer, size_t len, const char **key, const char **value)
{
    TRACE_PRINT ();
    char *cmd;
    int i;

    if (len > BUFFER_SIZE)
    {
        /* too large message */
        return CMD_INVALID;
    }
    if (len == BUFFER_SIZE)
    {
        if (memcmp (&buffer[BUFFER_SIZE - 1], g_lf, strlen (g_lf)))
        {
            /* too large message */
            return CMD_INVALID;
        }

        /* remove line feed */
        buffer[BUFFER_SIZE - 1] = '\0';
    }
    else
    {
        /* make it null-terminated */
        buffer[len] = '\0';

        char *lf_ptr = strstr (buffer, g_lf);
        if (lf_ptr == NULL)
        {
            return CMD_INCOMPLETE;
        }

        /* remove line feed */
        *lf_ptr = '\0';
    }

    cmd = strtok (buffer, " ");
    if (cmd == NULL)
    {
        /* no command found */
        return CMD_INVALID;
    }

    /* convert command to uppercase for case-insensitive comparison */
    for (i = 0; cmd[i]; i++)
    {
        cmd[i] = toupper (cmd[i]);
    }

    for (i = 0; i < CMD_COUNT; i++)
    {
        if (strcmp (cmd, g_cmds[i]) == 0)
        {
            *key = strtok (NULL, " ");
            if (*key == NULL)
            {
                /* no key found */
                return CMD_INVALID;
            }
            if (strlen (*key) > MAX_KEY_LEN)
            {
                /* too large key */
                return CMD_INVALID;
            }

            *value = strtok (NULL, " ");

            /* handle specific cases for READ and DELETE */
            if ((i == CMD_READ || i == CMD_DELETE) && *value != NULL)
            {
                /* READ or DELETE should not have a value */
                return CMD_INVALID;
            }

            /* handle specific cases for CREATE and UPDATE */
            if ((i == CMD_CREATE || i == CMD_UPDATE) && *value == NULL)
            {
                /* CREATE or UPDATE must have a value */
                return CMD_INVALID;
            }

            /* check for extra tokens after value */
            if (strtok (NULL, " ") != NULL)
            {
                /* extra tokens found */
                return CMD_INVALID;
            }

            /* return the corresponding command enum */
            return i;
        }
    }

    /* command not recognized */
    return CMD_INVALID;
}
/*---------------------------------------------------------------------------*/
struct skvs_ctx *
skvs_init (size_t hash_size, int delay)
{
    TRACE_PRINT ();
    struct skvs_ctx *ctx = calloc (1, sizeof (struct skvs_ctx));
    /* initialize the global hash table */
    ctx->table = hash_init (hash_size, delay);
    if (ctx->table == NULL)
    {
        DEBUG_PRINT ("Failed to initialize global hash table");
        return NULL;
    }

    return ctx;
}
/*---------------------------------------------------------------------------*/
int
skvs_destroy (struct skvs_ctx *ctx, int dump)
{
    TRACE_PRINT ();
    if (dump)
    {
        hash_dump (ctx->table);
    }
    if (hash_destroy (ctx->table) < 0)
    {
        return -1;
    }

    return 0;
}
/*---------------------------------------------------------------------------*/
int
skvs_serve (struct skvs_ctx *ctx, char *rbuf, size_t rlen, char *wbuf,
            size_t *wlen)
{
    TRACE_PRINT ();
    const char *key = NULL, *value = NULL;
    enum CMD cmd;
    int ret;

    /* parse the command */
    cmd = skvs_parse (rbuf, rlen, &key, &value);

    /* handle request */
    switch (cmd)
    {
    case CMD_INCOMPLETE:
        return 0;
    case CMD_CREATE:
        ret = hash_insert (ctx->table, key, value);
        if (ret > 0)
        {
            strcpy (wbuf, g_msgs[MSG_CREATE_OK]);
        }
        else if (ret == 0)
        {
            strcpy (wbuf, g_msgs[MSG_COLLISION]);
        }
        else
        {
            strcpy (wbuf, g_msgs[MSG_INTERNAL_ERR]);
        }
        break;
    case CMD_READ:
        ret = hash_search (ctx->table, key, wbuf);
        if (ret > 0)
        {
            ; // hash search has already copied the value to wbuf
        }
        else if (ret == 0)
        {
            strcpy (wbuf, g_msgs[MSG_NOT_FOUND]);
        }
        else
        {
            strcpy (wbuf, g_msgs[MSG_INTERNAL_ERR]);
        }
        break;
    case CMD_UPDATE:
        ret = hash_update (ctx->table, key, value);
        if (ret > 0)
        {
            strcpy (wbuf, g_msgs[MSG_UPDATE_OK]);
        }
        else if (ret == 0)
        {
            strcpy (wbuf, g_msgs[MSG_NOT_FOUND]);
        }
        else
        {
            strcpy (wbuf, g_msgs[MSG_INTERNAL_ERR]);
        }
        break;
    case CMD_DELETE:
        ret = hash_delete (ctx->table, key);
        if (ret > 0)
        {
            strcpy (wbuf, g_msgs[MSG_DELETE_OK]);
        }
        else if (ret == 0)
        {
            strcpy (wbuf, g_msgs[MSG_NOT_FOUND]);
        }
        else
        {
            strcpy (wbuf, g_msgs[MSG_INTERNAL_ERR]);
        }
        break;
    case CMD_INVALID:
    default:
        strcpy (wbuf, g_msgs[MSG_INVALID]);
        break;
    }

    strcat (wbuf, g_lf);
    *wlen = strlen (wbuf);

    return 1;
}