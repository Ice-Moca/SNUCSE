CC=gcc
CFLAGS= -Wall -Werror -pedantic -ansi -std=c99 -O2 -g

TARGET=p
SOURCES=main.c swap.c

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $(TARGET) $(SOURCES)

$(TARGETS): %: %.c
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm -rf $(TARGET)
