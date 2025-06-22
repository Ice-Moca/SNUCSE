/*---------------------------------------------------------------------------*/
/* skvslib.h                                                                 */
/* Author: Junghan Yoon, KyoungSoo Park                                      */
/*---------------------------------------------------------------------------*/
#ifndef _SKVSLIB_H
#define _SKVSLIB_H
/*---------------------------------------------------------------------------*/
#include "common.h"
#include "hashtable.h"
#include <ctype.h>
#include <errno.h>
#include <string.h>
/*---------------------------------------------------------------------------*/
/* response message indices */
enum MSG
{
    MSG_INVALID,
    MSG_CREATE_OK,
    MSG_COLLISION,
    MSG_NOT_FOUND,
    MSG_UPDATE_OK,
    MSG_DELETE_OK,
    MSG_INTERNAL_ERR,
    MSG_COUNT
};
/* command indices */
enum CMD
{
    CMD_INCOMPLETE = -2,
    CMD_INVALID,
    CMD_CREATE,
    CMD_READ,
    CMD_UPDATE,
    CMD_DELETE,
    CMD_COUNT
};
/*---------------------------------------------------------------------------*/
/* SKVS context */
struct skvs_ctx
{
    int sock;
    hashtable_t *table;
};
/*---------------------------------------------------------------------------*/
/**
 * initiates SKVS context including a thread-safe global hash table.
 * returns NULL when any internal errors occur.
 * returns the SKVS context pointer on success.
 */
struct skvs_ctx *skvs_init (size_t hash_size, int delay);
/*---------------------------------------------------------------------------*/
/**
 * destroys SKVS context and the hash table.
 * when set dump, dumps the hash table before destroy it.
 * returns -1 when any internal errors occur.
 * returns 0 on success.
 */
int skvs_destroy (struct skvs_ctx *ctx, int dump);
/*---------------------------------------------------------------------------*/
/**
 * On success, this function:
 * 1. writes the complete SKVS response to wbuf for the given request in rbuf.
 * 2. sets wlen to the length of the response.
 * 3. returns 1.
 *
 * When the given request in rbuf is incomplete, returns 0.
 */
int skvs_serve (struct skvs_ctx *ctx, char *rbuf, size_t rlen, char *wbuf,
                size_t *wlen);
/*---------------------------------------------------------------------------*/
#endif // _SKVSLIB_H