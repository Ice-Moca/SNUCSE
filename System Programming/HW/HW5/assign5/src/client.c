/*---------------------------------------------------------------------------*/
/* client.c                                                                  */
/* Author: Junghan Yoon, KyoungSoo Park                                      */
/* Modified by: (EunSu Yeo)                                                  */
/*---------------------------------------------------------------------------*/
#define _GNU_SOURCE
#include "common.h"
#include <arpa/inet.h>
#include <errno.h>
#include <fcntl.h>
#include <getopt.h>
#include <netdb.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
/*---------------------------------------------------------------------------*/
int
main (int argc, char *argv[])
{
    char *ip = DEFAULT_LOOPBACK_IP;
    int port = DEFAULT_PORT;
    int interactive = 0; /* Default is non-interactive mode */
    int opt;

    /*---------------------------------------------------------------------------*/
    /* free to declare any variables */

    /*---------------------------------------------------------------------------*/

    /* parse command line options */
    while ((opt = getopt (argc, argv, "i:p:th")) != -1)
    {
        switch (opt)
        {
        case 'i':
            ip = optarg;
            break;
        case 'p':
            port = atoi (optarg);
            if (port <= 1024 || port >= 65536)
            {
                perror ("Invalid port number");
                exit (EXIT_FAILURE);
            }
            break;
        case 't':
            interactive = 1;
            break;
        case 'h':
        default:
            printf ("Usage: %s [-i server_ip_or_domain (%s)] "
                    "[-p port (%d)] [-t]\n",
                    argv[0], DEFAULT_LOOPBACK_IP, DEFAULT_PORT);
            exit (EXIT_FAILURE);
        }
    }

    /*---------------------------------------------------------------------------*/
    /* edit here */
    struct addrinfo hints = {0}, *res, *rp;
    char portstr[16];
    snprintf(portstr, sizeof(portstr), "%d", port);
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;
    int ret = getaddrinfo(ip, portstr, &hints, &res);
    if (ret != 0) {
        fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(ret));
        return 1;
    }
    int sockfd = -1;
    for (rp = res; rp != NULL; rp = rp->ai_next) {
        sockfd = socket(rp->ai_family, rp->ai_socktype, rp->ai_protocol);
        if (sockfd == -1) continue;
        if (connect(sockfd, rp->ai_addr, rp->ai_addrlen) == 0) break;
        close(sockfd);
        sockfd = -1;
    }
    freeaddrinfo(res);
    if (sockfd == -1) {
        perror("connect failed");
        return 1;
    }

    if (interactive)
        printf("Connected to %s:%d\n", ip, port);

    char buf[BUFFER_SIZE];
    while (1) {
        if (interactive) printf("Enter command: ");
        if (!fgets(buf, sizeof(buf), stdin)) break;
        size_t len = strlen(buf);
        if (len == 0 || (len == 1 && buf[0] == '\n')) break;

        ssize_t sent = 0;
        while (sent < len) {
            ssize_t n = write(sockfd, buf + sent, len - sent);
            if (n < 0) goto done;
            sent += n;
        }

        ssize_t rcvd = read(sockfd, buf, sizeof(buf) - 1);
        if (rcvd == 0) {
            if (interactive) printf("Server reply: Connection closed by server\n");
            break;
        }
        if (rcvd < 0) goto done;
        buf[rcvd] = '\0';

        if (interactive)
            printf("Server reply: %s", buf);
        else
            fwrite(buf, 1, rcvd, stdout);
    }
done:
    close(sockfd);
    /*---------------------------------------------------------------------------*/

    return 0;
}
