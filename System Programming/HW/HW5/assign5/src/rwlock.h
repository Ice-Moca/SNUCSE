/*---------------------------------------------------------------------------*/
/* rwlock.h                                                                  */
/* Author: Junghan Yoon, KyoungSoo Park                                      */
/*---------------------------------------------------------------------------*/
#ifndef _RWLOCK_H
#define _RWLOCK_H
/*---------------------------------------------------------------------------*/
#include "common.h"
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#define WRITER_RING_SIZE NUM_THREADS
/*---------------------------------------------------------------------------*/
typedef struct
{
    int read_count;         // number of current/pending read threads
    int write_count;        // number of write threads
    pthread_mutex_t lock;   // mutex lock for protection
    pthread_cond_t readers; // condvar for threads waiting read
    pthread_cond_t writers; // condvar for threads waiting write

    /* pending writer ring */
    pthread_t *writer_ring; // thread IDs array
    int writer_ring_head;   // position to insert
    int writer_ring_tail;   // position to evict

    /* delay for semantic test */
    int delay;
} rwlock_t;
/*---------------------------------------------------------------------------*/
/**
 * initializes rwlock.
 * returns -1 when any internal errors occur.
 * returns 0 on success.
 */
int rwlock_init (rwlock_t *rw, int delay);
/*---------------------------------------------------------------------------*/
/**
 * acquires read lock.
 * returns -1 when any internal errors occur.
 * returns 0 on success.
 */
int rwlock_read_lock (rwlock_t *rw);
/*---------------------------------------------------------------------------*/
/**
 * releases read lock.
 * returns -1 when any internal errors occur.
 * returns 0 on success.
 */
int rwlock_read_unlock (rwlock_t *rw);
/*---------------------------------------------------------------------------*/
/**
 * acquires write lock.
 * returns -1 when any internal errors occur.
 * returns 0 on success.
 */
int rwlock_write_lock (rwlock_t *rw);
/*---------------------------------------------------------------------------*/
/**
 * releases write lock.
 * returns -1 when any internal errors occur.
 * returns 0 on success.
 */
int rwlock_write_unlock (rwlock_t *rw);
/*---------------------------------------------------------------------------*/
/**
 * destroys rwlock.
 * returns -1 when any internal errors occur.
 * returns 0 on success.
 */
int rwlock_destroy (rwlock_t *rw);
/*---------------------------------------------------------------------------*/
#endif // _RWLOCK_H