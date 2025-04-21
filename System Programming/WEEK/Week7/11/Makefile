CC=gcc
CFLAGS= -Wall -Werror -pedantic -std=c99 -O2 -fcommon -pipe

TARGET=coupang
OBJECTS=trim.o
SOURCES=coupang.c

all: $(TARGET)

$(TARGET): $(SOURCES) $(OBJECTS)
	$(CC) $(CFLAGS) -o $(TARGET) $(SOURCES) $(OBJECTS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(TARGET) $(OBJECTS)