CC = gcc
CFLAGS = -Wall -Werror -pedantic -ansi -std=c99 -pthread -O2

TARGETS = layout

all: $(TARGETS)

$(TARGETS): %: %.c
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm -rf $(TARGETS)
	rm -rf *.txt
