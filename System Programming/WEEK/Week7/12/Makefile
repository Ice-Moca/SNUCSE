CC=gcc
CFLAGS= -Wall -Werror -pedantic -std=c99

libvector.so: 
	$(CC) $(CFLAGS) -shared -o libvector.so addvec.c mulvec.c


vectormath: libvector.so
	$(CC) $(CFLAGS) -g -o vectormath vectormath.c -L. -lvector

vectormathrt: libvector.so
	$(CC) $(CFLAGS) -g -o vectormathrt vectormathrt.c -ldl

vectormathrt_compile_error: libvector.so
	$(CC) $(CFLAGS) -g -o vectormathrt vectormathrt_compile_error.c -ldl

helloc:
	$(CC) $(CFLAGS) -DCOMPILETIME -c mymalloc.c
	$(CC) $(CFLAGS) -I. -o helloc hello.c mymalloc.o

runc: helloc
	./helloc

hellol:
	$(CC) $(CFLAGS) -DLINKTIME -c mymalloc.c
	$(CC) $(CFLAGS) -Wl,--wrap,malloc -Wl,--wrap,free -o hellol hello.c mymalloc.o

runl: hellol
	./hellol

hellor:
	$(CC) $(CFLAGS) -DRUNTIME -shared -fPIC -o mymalloc.so mymalloc.c -ldl
	$(CC) $(CFLAGS) -o hellor hello.c

runr: hellor
	LD_PRELOAD="./mymalloc.so" ./hellor

hellor_buggy:
	$(CC) $(CFLAGS) -g -DRUNTIME -shared -fPIC -o mymalloc.so mymalloc_buggy.c -ldl
	$(CC) $(CFLAGS) -g -o hellor hello.c

runr_buggy: hellor_buggy
	LD_PRELOAD="./mymalloc.so" ./hellor

hellor_debug:
	$(CC) $(CFLAGS) -DRUNTIME -shared -fPIC -o mymalloc.so mymalloc_for_debug.c -ldl
	$(CC) $(CFLAGS) -o hellor hello.c

runr_debug: hellor_debug
	LD_PRELOAD="./mymalloc.so" ./hellor

clean:
	rm -rf *.so vectormath vectormathrt helloc hellol hellor
	rm -rf *.o