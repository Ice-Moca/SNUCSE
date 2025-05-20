CC = gcc
CFLAGS = -O2 -std=gnu99 -Iinclude
SRCDIR = src
TARGET = main
SOURCES = $(SRCDIR)/main.c $(SRCDIR)/hw3.c

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) $(SOURCES) -o $(TARGET)

run: $(TARGET)
	./$(TARGET) < input/1.in

clean:
	rm -f $(TARGET)
