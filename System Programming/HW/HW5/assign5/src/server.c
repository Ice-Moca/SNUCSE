/*---------------------------------------------------------------------------*/
/* server.c                                                                  */
/* Author: Junghan Yoon, KyoungSoo Park                                      */
/* Modified by: (EunSu Yeo)                                                  */
/*---------------------------------------------------------------------------*/
#define _GNU_SOURCE
#include "common.h"
#include "skvslib.h"
#include <arpa/inet.h>
#include <errno.h>
#include <getopt.h>
#include <pthread.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#include <unistd.h>
/*---------------------------------------------------------------------------*/
struct thread_args
{
    int listenfd;
    int idx;
    struct skvs_ctx *ctx;

    /*---------------------------------------------------------------------------*/
    /* free to use */

    /*---------------------------------------------------------------------------*/
};
/*---------------------------------------------------------------------------*/
volatile static sig_atomic_t g_shutdown = 0;
/*---------------------------------------------------------------------------*/
void *
handle_client (void *arg)
{
    TRACE_PRINT ();
    struct thread_args *args = (struct thread_args *)arg;
    struct skvs_ctx *ctx = args->ctx;
    int idx = args->idx;
    int listenfd = args->listenfd;
    /*---------------------------------------------------------------------------*/
    /* free to declare any variables */
    
    /*---------------------------------------------------------------------------*/

    free (args);
    printf ("%dth worker ready\n", idx);

    /*---------------------------------------------------------------------------*/
    /* edit here */
    fflush(stdout);

    while (!g_shutdown) {
        struct sockaddr_in client_addr;
        socklen_t client_len = sizeof(client_addr);
        int clientfd = accept(listenfd, (struct sockaddr *)&client_addr, &client_len);
        if (clientfd < 0) {
            if (errno == EINTR || errno == EAGAIN) continue;
            if (g_shutdown) break;
            continue;
        }
        while (1) {
            char rbuf[BUFFER_SIZE];
            ssize_t rlen = read(clientfd, rbuf, BUFFER_SIZE);
            if (rlen == 0) {
                printf("Connection closed by client\n");
                break;
            }
            if(rlen<0 && errno == EAGAIN) {
                // interrupted by signal, retry read
                continue;
            }
            // // === 디버깅용 로그 ===
            // if (rlen > 0)
            //     printf("SERVER DEBUG: rlen=%ld, buf='", rlen), fwrite(rbuf, 1, rlen, stdout), printf("'\n");
            // else
            //     printf("SERVER DEBUG: rlen=%ld (errno=%d)\n", rlen, errno);
            // fflush(stdout);
            // // ===================
            if (rlen <= 0) break;
            if (rlen == 1 && rbuf[0] == '\n') break;

            char wbuf[BUFFER_SIZE];
            size_t resp_len = 0;
            int ret = skvs_serve(ctx, rbuf, rlen, wbuf, &resp_len);

            if (ret == 0) {
                // incomplete: 입력 누적 (개행 없는 경우 등), 응답 보내지 않고 continue
                continue;
            }
            // ret > 0(정상), ret < 0(에러) 모두 write/send 실행
            ssize_t sent = 0;
            while (sent < resp_len) {
                ssize_t n = write(clientfd, wbuf + sent, resp_len - sent);
                if (n < 0) break;
                sent += n;
            }
            if (ret < 0) break; // 내부 에러시 연결 종료 (참고: INVALID CMD는 에러 아님)
        }
        close(clientfd);
    }
    /*---------------------------------------------------------------------------*/

    return NULL;
}
/*---------------------------------------------------------------------------*/
/* Signal handler for SIGINT */
void
handle_sigint (int sig)
{
    TRACE_PRINT ();
    printf ("\nReceived SIGINT, initiating shutdown...\n");
    g_shutdown = 1;
}
/*---------------------------------------------------------------------------*/
int
main (int argc, char *argv[])
{
    size_t hash_size = DEFAULT_HASH_SIZE;
    char *ip = DEFAULT_ANY_IP;
    int port = DEFAULT_PORT, opt;
    int num_threads = NUM_THREADS;
    int delay = RWLOCK_DELAY;
    int listen_fd, optval;
    struct timeval to;
    /*---------------------------------------------------------------------------*/
    /* free to declare any variables */

    /*---------------------------------------------------------------------------*/

    /* parse command line options */
    while ((opt = getopt (argc, argv, "p:t:s:d:h")) != -1)
    {
        switch (opt)
        {
        case 'p':
            port = atoi (optarg);
            break;
        case 't':
            num_threads = atoi (optarg);
            break;
        case 's':
            hash_size = atoi (optarg);
            if (hash_size <= 0)
            {
                perror ("Invalid hash size");
                exit (EXIT_FAILURE);
            }
            break;
        case 'd':
            delay = atoi (optarg);
            break;
        case 'h':
        default:
            printf ("Usage: %s [-p port (%d)] "
                    "[-t num_threads (%d)] "
                    "[-d rwlock_delay (%d)] "
                    "[-s hash_size (%d)]\n",
                    argv[0], DEFAULT_PORT, NUM_THREADS, RWLOCK_DELAY,
                    DEFAULT_HASH_SIZE);
            exit (EXIT_FAILURE);
        }
    }

    /* set listen fd with Reuse addr, port, and timeout options. */
    listen_fd = socket (AF_INET, SOCK_STREAM, 0);
    if (listen_fd == -1)
    {
        perror ("Could not create socket");
        return -1;
    }

    optval = 1;
    if (setsockopt (listen_fd, SOL_SOCKET, SO_REUSEADDR, &optval,
                    sizeof (optval))
        != 0)
    {
        perror ("setsockopt SO_REUSEADDR failed");
        close (listen_fd);
        return -1;
    }
    optval = 1;
    if (setsockopt (listen_fd, SOL_SOCKET, SO_REUSEPORT, &optval,
                    sizeof (optval))
        != 0)
    {
        perror ("setsockopt SO_REUSEPORT failed");
        close (listen_fd);
        return -1;
    }

    /* set timeout for client socket for escape on SIGINT */
    to.tv_sec = TIMEOUT;
    to.tv_usec = 0;
    if (setsockopt (listen_fd, SOL_SOCKET, SO_RCVTIMEO, &to, sizeof (to)) < 0)
    {
        perror ("setsockopt SO_RCVTIMEO failed");
        close (listen_fd);
        return -1;
    }

    /*---------------------------------------------------------------------------*/
    /* edit here */
    signal(SIGINT, handle_sigint);

    struct sockaddr_in servaddr = {0};
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(port);
    servaddr.sin_addr.s_addr = inet_addr(ip);

    if (bind(listen_fd, (struct sockaddr *)&servaddr, sizeof(servaddr)) < 0) {
        perror("bind failed");
        close(listen_fd);
        return -1;
    }
    if (listen(listen_fd, NUM_BACKLOG) < 0) {
        perror("listen failed");
        close(listen_fd);
        return -1;
    }

    struct skvs_ctx *ctx = skvs_init(hash_size, delay);
    if (!ctx) {
        perror("Failed to init ctx");
        close(listen_fd);
        return -1;
    }

    pthread_t threads[num_threads];
    for (int i = 0; i < num_threads; ++i) {
        struct thread_args *args = malloc(sizeof(struct thread_args));
        args->listenfd = listen_fd;
        args->idx = i;
        args->ctx = ctx;
        pthread_create(&threads[i], NULL, handle_client, args);
    }
    for (int i = 0; i < num_threads; ++i) pthread_join(threads[i], NULL);

    skvs_destroy(ctx, 1);
    close(listen_fd);
    /*---------------------------------------------------------------------------*/

    return 0;
}
