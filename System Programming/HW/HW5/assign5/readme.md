# Lab 5: Simple Key-Value Store

The purpose of this lab is to familiarize ourselves with TCP/IP networking, the client-server programming model, and thread-safe data structures. To achieve the goal, we implement a simple server that serves as a key-value store and a client that requests the value for a key. Your server should be able to handle multiple concurrent clients (~10).

You will learn
   * how to communicate with clients using the socket API.
   * how to handle multiple readers and writers on the shared data.


## Important Dates

| Date | Description |
|:---  |:--- |
| Monday, June 16, 21:00 | Submission deadline |

## Logistics

### Hand-out

Start by downloading the tarball from Classum and read the instructions here carefully.


### Submission

Submit on Classum. We accept no late submission.


## Background

### Socket interface

```
        Client                         Server
    +-------------+               +-------------+
    |    socket   |               |    socket   |
    +-------------+               +-------------+
           |                             |
           |                             v
           |                      +-------------+
           |                      |     bind    |
           |                      +-------------+
           |                             |
           |                             v
           |                      +-------------+
           |                      |    listen   |
           |                      +-------------+
           |                             |
           v         Connection          v
    +-------------+    request    +-------------+   Await connection
    |   connect   |-------------->|    accept   |   request from next client (blocking)
    +-------------+               +-------------+
           |                             |
           v                             v
    +-------------+               +-------------+
 /->|     send    |-------------->|     recv    |<-\
|   +-------------+               +-------------+   |
|          |                             |          |
|          v                             v          |
|   +-------------+               +-------------+   |
 \--|     recv    |<--------------|     send    |--/
    +-------------+               +-------------+
           |                             |
           v                             v
    +-------------+      EOF      +-------------+
    |    close    |-------------->|     recv    |
    +-------------+               +-------------+
                                         |
                                         v
                                  +-------------+
                                  |    close    |
                                  +-------------+
```

You are assumed to know how the socket API works. If not, we recommend you to review Beej's Guide to Network Programming (https://beej.us/guide/bgnet/) to understand each function before you start.
Specifically, calling recv() (or read()) once might not receive the entire application message for many reasons. In the same context, calling send() (or write()) once might not send all application messgage at once. You should always check the return value after calling recv() and send() even when handling small data. For more details, please refer to the lecture notes related to network programming. CSAPP 10.5 also shows a simple example of robust IO.


### RW Lock (Read-Write Lock) for many readers and writers

The RW lock is a great tool for synchronizing accesses to shared resources by multiple threads. It allows concurrent read tasks when there is no write task, but it restricts a write task to be done exclusively. Our rwlock.c and rwlock.h are very similar to the existing POSIX pthread_rwlock API. If you are not familiar with the RW lock, please refer to the oracle document (https://docs.oracle.com/cd/E37838_01/html/E61057/sync-124.html) or IBM document (https://www.ibm.com/docs/en/aix/7.3?topic=p-pthread-rwlock-rdlock-pthread-rwlock-tryrdlock-subroutines) before you start.


## SKVS Overview

_SKVS_ is a simple socket-based server that serves key-value read/lookup or write/update requests from the clients. The SKVS server repeatedly listens and accepts clients until a _SIGINT_ signal (Ctrl+C) is received. On exit, it prints out the statistics regarding how it worked.

### Overall Architecture of _SKVS_ server

```
        Client                                           
    +-------------+                                                   SKVS main thread      
    |    socket   |                           SKVS worker threads      +-------------+      
    +-------------+                            /       / / / /         |    socket   |      
           |                                   \  ...  \ \ \ \         +-------------+      
           |                                   /       / / / /                |             
           |                                   v       v v v v                v             
           |                                                           +-------------+      
           |                                                           |     bind    |      
           |                                                           +-------------+        
           |                                                                  |
           |                                                                  v
           |                                                           +-------------+
           |                                           - - - - - - - - |    listen   |
           |                                         /     listenfd    +-------------+
           v                                        v                   
    +-------------+  Connection request     +-------------+
    |   connect   |------------------------>|    accept   |
    +-------------+                         +-------------+
           |                                       |       
           v                                       v       
    +-------------+   [CMD] [key] [value]   +-------------+          +-------------+
 /->|     send    |------------------------>|     recv    |--------->|   ||   ||   |  global
|   +-------------+                         +-------------+          | ==  ===  == |  hash table
|          |                                       ^                 |   ||   ||   |  for entries of
|          v                                       |                 | ==  ===  == |  key-value pairs
|   +-------------+         response        +-------------+          |   ||   ||   |  with
 \--|     recv    |<------------------------|     send    |<---------|             |  fine-grained
    +-------------+                         +-------------+          +-------------+  rw lock
           | double                                |
           v empty line                            v
    +-------------+                         +-------------+
    |    close    |------------------------>|     recv    |
    +-------------+                         +-------------+
                                                   |
                                                   v
                                            +-------------+
                                            |    close    |
                                            +-------------+
```

## SKVS Specification

1. _SKVS_ uses one connection per one client.
2. Each _SKVS_ connection runs in keep-alive mode until typing empty line (\n) or EOF (Ctrl+D) on the client.
3. _SKVS_ protocol is half-duplex. After sending request, client should wait for the response.
4. _SKVS_ protocol is text-based protocol.
5. Server should be stateful. Key-value pairs should be accessible by other clients.
6. Default service port is 8080.

### Operation
1. The server creates a global hash table with 4096 buckets for storing key-value entries.
   1) The global hash table should support thread-safe access to both read and write operations. For performance, it uses fine-grained locks, which employs a separate lock for each bucket.
2. The server creates a _listening_ socket that will be shared by all worker threads. The default port number is 8080, but it can be adjusted by -p option.
3. The server creates a thread pool of 10 _SKVS_ worker threads. The listening socket will be passed to the _start_routine_ of each thread as part of an _argument_.
   1) After creating the worker thread pool, the main thread waits for them to finish (by join()).
4. When a client connects to the _SKVS_ server, the responsible worker thread _accepts_ the client connection.
5. After connection establishment, the client sends a key-value command to the server. _SKVS_ supports 4 operations: _CREATE_, _READ_, _UPDATE_, and _DELETE_.
6. The responsible worker thread receives the command and parses it.
   1) For _CREATE_, it allocates a key-value entry and inserts it to the hashtable. Then, it responds with _CREATE OK_.
   2) For _READ_, it searches the responsible key-value entry and responds with the value. Then, it responds with the [ _value_ ].
   3) For _UPDATE_, it searches the responsible key-value entry and updates the value. Then, it responds with _UPDATE OK_.
   4) For _DELETE_, it searches the responsible key-value entry and deletes the value. Then, it responds with _DELETE OK_.
   5) If a key-value pair already exists, it responds with _COLLISION_ for a _CREATE_ command.
   6) For any others, it reponds with _INVALID CMD_.
   7) When the search fails, it responds with _NOT FOUND_.
   8) When any internal error occurs, it reponds with _INTERNAL ERR_. (It will not be evaluated.)
7. Repeat 5 ~ 6.
8. If the client feeds an empty line or EOF (e.g., by typing Ctrl+D) into the input stream, it closes the socket and exits.
9. When Ctrl+C (SIGINT) is pressed on the server side, all worker threads will close.


### Requirements
Your server should serve 10 concurrent clients. It should be able to receive or send L7 messages of arbitrary length. Your global hashtable should be able to handle concurrent accesses. To this end, you should implement correct rwlock (read-write lock) library and hashtable library.


### Scope
1. Current _SKVS_ architecture has no issue in handling concurrent flows more than the number of worker threads. To this end, one worker thread should be able to handle multiple flows by itself. Thus, a complete implementation would require adopting asynchronous and non-blocking APIs. However, it is hard to fully grasp the concept of asynchronous networking and the implementation might be very error-prone for beginners. For this assignment, you may implement your _SKVS_ server to handle as many concurrent flows as the number of worker threads which are statically initiated at the begining.
2. In the same context with above, we exclude implementing non-blocking RW lock. You do not need to consider writer's starvation for this assignment. We will not test that case.
3. The key and value are assumed to be ASCII string. There are many well known L7 protocols for a key-value store, such as memcached or redis. They support any binaries for a key and a value. However, for this assignment, we simplify L7 protocol processing as much as possible.
4. Our RW lock is reader-priority, which shows best performance when read operations are much more frequent than write operations. To avoid write starvation, there is writer-priority RW lock, but this is out of scope. Implement the RW lock for in reader-priority mode.


### L7 MSG formats
1. Basically, requests should be formatted like "[ _CMD_ ] [ _key_ ] [ _value_ ]\n" for _CREATE_, _UPDATE_, and _DELETE_. For _READ_, the requests should be like "READ [ _key_ ]\n".
2. We provide _SKVS_ APIs such as skvs_serve() which returns a well-formatted _SKVS_ response for the given request. 
3. The lengths of [ _key_ ] is at most 32B.
4. The length of SKVS MSG is at most 4096B.
5. Do not modify the default response messages returned by skvs_serve() function.

You do not need to manually parse the requests. skvs_serve() will parse the request from the given buffer. It returns NULL if the request is incomplete. (e.g., no "\n" found, or too large request) If the request is complete, it will return a pointer to the corresponding command.
Below are 7 fixed messages for three commands; _CREATE_, _UPDATE_, and _DELETE_.

"INVALID CMD"
"CREATE OK"
"COLLISION"
"NOT FOUND"
"UPDATE OK"
"DELETE OK"
"INTERNAL ERR"

Since they are defined as constant literals, you do not need to free them.

For _READ_ command, skvs_serve() returns a pointer to the [ _value_ ] stored in the hashtable.
Again, you do not need to free it. It will be freed only if _SKVS_ server receives _DELETE_ command.
If there is no key-value pair matches with the given [ _key_ ], the server should return "NOT FOUND".

Note that the return value of skvs_serve() has no line feed. You should send not only the literals, but also a line feed to comply the _SKVS_ protocol.


### Server/Client behavior
Please refer to the server.c and client.c. They show the usage at option parsing part. Do not modify the usage.
When more than 10 clients try to connect to the server, the each worker thread is supposed to be able to handle it after closing the previous sockets.
After an _SKVS_ client connects to the server, it can send 4 commands; _CREATE_, _READ_, _UPDATE_, and _DELETE_ in a format of [ _CMD_ ] [ _key_ ] [ _value_ ], or [ _CMD_ ] [ _key_ ] for _READ_.
Each command should be manually typed when using the given default client.
The reference client runs in interactive mode when giving -t option.
Without -t option, it runs in silent mode. In this mode, it only prints the server reply (e.g., CREATE OK) without "Enter command: " or "Server reply: ".

The request format, [ _CMD_ ] [ _key_ ] [ _value_ ] should be handled as ASCII strings. [ _CMD_ ] is **case-insensitive**, and [ _key_ ], [ _value_ ] are **case-sensitive**. However, you don't need to worry about it, since it will be handled by skvs_serve().
For reference, we upload our binary on eTL. If you are concerned about any ambiguous semantics, please refer to the reference binary.


### Usage

```
./server -h
Usage: ./server [-p port (8080)] [-t num_threads (10)] [-d rwlock_delay (0)] [-s hash_size (1024)]
```

The parameter following -d option gives delay to rwlock_read_unlock() and rwlock_write_unlock() this is used to check semantic of your rwlock APIs.


```
./client -h
Usage: ./client [-i server_ip_or_domain (127.0.0.1)] [-p port (8080)] [-t]
```

The -t option makes the client run in interactive mode. This is for your better understanding of _SKVS_.
Your program may not support interactive mode, because I will run your client without -t option for grading.



### Output
```
./server
0th worker ready
1th worker ready
2th worker ready
3th worker ready
4th worker ready
5th worker ready
6th worker ready
7th worker ready
8th worker ready
9th worker ready
```

Below is an example.

```
./client -t
Connected to 127.0.0.1:8080
Enter command: CREATE junghan enfj
Server reply: CREATE OK
Enter command: creATE seongjong entp
Server reply: CREATE OK
Enter command: create jongki esfj
Server reply: CREATE OK
Enter command: CRAETE juyoung infp
Server reply: INVALID CMD
Enter command: READ junghan
Server reply: enfj
Enter command: READ seongjong
Server reply: entp
Enter command: UPDATE seongjong cute
Server reply: UPDATE OK
Enter command: READ seongjong
Server reply: cute
Enter command: DELETE junghan
Server reply: DELETE OK
Enter command: READ junghan
Server reply: NOT FOUND
```

We have prepared the reference client program, and _SKVS_ library as template code. Just modify **server.c**, **client.c**, **hashtable.c**, and **rwlock.c**. You are not allowed to modify any other source files.


## Handout Overview

The handout contains the following files and directories

| File/Directory | Description |
|:---  |:--- |
| README.md | this file |
| src/Makefile | All-in-one Makefile for libraries and applications. Do not edit this file. |
| src/client.c | Client-side implemention. **Implement your solution by editing this file.** |
| src/server.c | Server-side implemention. **Implement your solution by editing this file.** |
| src/common.h | Header file for applications. Do not edit this file. |
| src/skvslib.c | SKVS library which uses hash table library. Do not edit this file. |
| src/skvslib.h | SKVS library header file. Do not edit this file. |
| src/hashtable.c | Thread-safe hash table library which uses rwlock library. **Implement your solution by editing this file.** |
| src/hashtable.h | Thread-safe hash table library header file. Do not edit this file. |
| src/rwlock.c | rwlock library which uses pthread API. **Implement your solution by editing this file.** |
| src/rwlock.h | rwlock library header file. Do not edit this file. |
| src/rwtest.sh | You can use it for testing your rwlock. Run your server with -d 5.  |


## Hints

### First of all, make sure your worker thread and client can communiate with each other.
1. Starts from implementing client.c using the reference server and client binary. You can use -t option on the reference client. It will help you understand _SKVS_ protocol better.
2. Implement server.c using the reference client binary, or your own client.
3. Then, make sure your server can handle multiple concurrent clients.


### server.c

In server.c, focus on handling sockets and threads using the socket API and the pthread library. Note that recv() and send() do not guarantee that the L7 message is completely received or sent. You should handle the case where the L7 message is incomplete. To be robust, your server and client must be able to receive or send complete L7 messages of arbitrary length at any time.

### client.c

Focus on socket programming. Much easier than server.

### hashtable.c

In hashtable.h, there are simple descriptions of the functions defined in hashtable.c. Also, you should respect the usage of hashtable functions by checking _SKVS_ library. Specifically, skvs_serve() uses all of the functions defined in hashtable.c. You should allocate memory for [ _key_ ] and [ _value_ ] on insert(), while free them on delete(). Update() should allocate new memory for the new value after freeing the memory for the old value.

### rwlock.c

In rwlock.h, there are simple descriptions of the functions defined in rwlock.c. Also, you should repect the usage of hashtable functions by checking hashtable.c file.
1) rwlock_read_lock() can get read lock only when there is no writer. It should increase the reader counter after acquiring read lock.
2) rwlock_read_unlock() should decrease the reader counter first and check if the reader counter is zero. If so, it should send a signal to the oldest threads waiting for writing.
3) rwlock_write_lock() can get write lock only when there is neither reader nor writer. It should increase the writer counter after acquiring write lock.
4) rwlock_write_unlock() should decrease the writer counter first and check if the writer counter is zero. If so, it should send a signal to threads waiting for reading first, then send another signal to the oldest thread waiting for writing.

### _SKVS_ library call

You do not need to manually access the hashtable. skvs_serve() will parse the request and create/read/update/delete an entry at the hashtable.

### C library calls

To give you some insight, we provide a list of C library calls that you might find helpful to solve this lab. Read the man pages carefully to learn how exactly the functions operate.

<table>
  <thead>
    <tr>
      <th align="left">Topic</th>
      <th align="left">C library call</th>
      <th align="left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="5">
        String operations
      </td>
      <td>
        <code>strstr()</code>
      </td>
      <td>
        find a target string in a long string
      </td>
    </tr>
    <tr>
      <td>
        <code>strtok()</code>
      </td>
      <td>
        tokenize string by delimiter
      </td>
    </tr>
    <tr>
      <td>
        <code>strcmp() or strncmp()</code>
      </td>
      <td>
        compare two strings (by n characters for strncmp)
      </td>
    </tr>
    <tr>
      <td>
        <code>strdup()</code>
      </td>
      <td>
        duplicate the target string with malloc inside
      </td>
    </tr>
    <tr>
      <td>
        <code>strcpy()</code>
      </td>
      <td>
        duplicate the target string to existing memory
      </td>
    </tr>
    <tr>
      <td rowspan="11">
        Concurrent programming
      </td>
      <td>
        <code>pthread_create()</code>
      </td>
      <td>
        create a new thread
      </td>
    </tr>
    <tr>
      <td>
        <code>pthread_detach()</code>
      </td>
      <td>
        detach a thread
      </td>
    </tr>
    <tr>
      <td>
        <code>pthread_join()</code>
      </td>
      <td>
        wait a thread to be joined
      </td>
    </tr>
    <tr>
      <td>
        <code>pthread_exit()</code>
      </td>
      <td>
        terminate the calling thread
      </td>
    </tr>
    <tr>
      <td>
        <code>pthread_mutex_init()</code>
      </td>
      <td>
        create a mutex
      </td>
    </tr>
    <tr>
      <td>
        <code>pthread_mutex_lock()</code>
      </td>
      <td>
        lock a mutex
      </td>
    </tr>
    <tr>
      <td>
        <code>pthread_mutex_unlock()</code>
      </td>
      <td>
        unlock a mutex
      </td>
    </tr>
    <tr>
      <td>
        <code>pthread_cond_init()</code>
      </td>
      <td>
        create a condition variable
      </td>
    </tr>
    <tr>
      <td>
        <code>pthread_cond_wait()</code>
      </td>
      <td>
        wait on a condition variable
      </td>
    </tr>
    <tr>
      <td>
        <code>pthread_cond_signal()</code>
      </td>
      <td>
        unblock a thread waiting for a condition variable
      </td>
    </tr>
    <tr>
      <td>
        <code>pthread_cond_broadcast()</code>
      </td>
      <td>
        unblock all threads waiting for a condition variable
      </td>
    </tr>
  </tbody>
</table>

## Final words

Network & concurrent programming is not an easy task. We don't know exactly how it will behave and therefore makes it hard to debug. Start working on lab early and actively consult TAs if you seek any assistance.

<div align="center" style="font-size: 1.75em;">

**Happy coding!**
</div>
