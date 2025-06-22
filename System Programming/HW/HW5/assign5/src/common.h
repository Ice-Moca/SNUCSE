/*---------------------------------------------------------------------------*/
/* common.h                                                                  */
/* Author: Junghan Yoon, KyoungSoo Park                                      */
/*---------------------------------------------------------------------------*/
#ifndef _COMMON_H
#define _COMMON_H
/*---------------------------------------------------------------------------*/
#include <errno.h>
/*---------------------------------------------------------------------------*/
#define MAX_KEY_LEN 32
#define BUFFER_SIZE 4096
#define DEFAULT_PORT 8080
#define DEFAULT_LOOPBACK_IP "127.0.0.1"
#define DEFAULT_ANY_IP "0.0.0.0"
#define NUM_BACKLOG 20
#define NUM_THREADS 10
#define RWLOCK_DELAY 0
#define TIMEOUT 1
/*---------------------------------------------------------------------------*/
#ifdef DEBUG
#define DEBUG_PRINT(...)                                                      \
    do                                                                        \
    {                                                                         \
        fprintf (stderr, "[%s:%d] %s: ", __FILE__, __LINE__, __func__);       \
        fprintf (stderr, __VA_ARGS__);                                        \
        fprintf (stderr, "\n");                                               \
    } while (0)
#else
#define DEBUG_PRINT(...) (void)0
#endif
#ifdef TRACE
#define TRACE_PRINT()                                                         \
    fprintf (stdout, "[%s:%d] %s()\n", __FILE__, __LINE__, __func__)
#else
#define TRACE_PRINT() (void)0
#endif
/*---------------------------------------------------------------------------*/
#endif // _COMMON_H