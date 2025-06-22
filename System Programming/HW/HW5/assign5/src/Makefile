# Compiler
CC = gcc800

# Compiler flags
CFLAGS = -g -O0 -pthread -D_POSIX_C_SOURCE=200809L

# CFLAGS += -DDEBUG
# CFLAGS += -DTRACE

# Server source files
SERVER_SRC = server.c skvslib.c hashtable.c rwlock.c

# Client source files
CLIENT_SRC = client.c

# Object files
SERVER_OBJ = $(SERVER_SRC:.c=.o)
CLIENT_OBJ = $(CLIENT_SRC:.c=.o)

# Executables
SERVER_TARGET = server
CLIENT_TARGET = client

# Default target: build both server and client
all: $(SERVER_TARGET) $(CLIENT_TARGET)

# Build the server executable
$(SERVER_TARGET): $(SERVER_OBJ)
	$(CC) $(CFLAGS) -o $(SERVER_TARGET) $(SERVER_OBJ)

# Build the client executable
$(CLIENT_TARGET): $(CLIENT_OBJ)
	$(CC) $(CFLAGS) -o $(CLIENT_TARGET) $(CLIENT_OBJ)

# Compile individual object files
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Submit target
submit: clean all
	@if [ -z "$(ID)" ]; then \
		echo "Error: ID not provided. Example: make submit ID=202435498"; \
		exit 1; \
	fi
	@echo "Creating submission for ID: $(ID)"
	@mkdir -p $(ID)_assign5
	@cp server.c client.c hashtable.c rwlock.c $(ID)_assign5/
	@tar -zcvf $(ID)_assign5.tar.gz $(ID)_assign5
	@if [ -d "$(ID)_assign5" ]; then rm -rf $(ID)_assign5; fi
	@echo "Submission package $(ID)_assign5.tar.gz created successfully."

# Clean up build artifacts
clean:
	@if [ -f "$(SERVER_TARGET)" ]; then rm -f $(SERVER_TARGET); fi
	@if [ -f "$(CLIENT_TARGET)" ]; then rm -f $(CLIENT_TARGET); fi
	@if [ -n "$(SERVER_OBJ)" ]; then rm -f $(SERVER_OBJ); fi
	@if [ -n "$(CLIENT_OBJ)" ]; then rm -f $(CLIENT_OBJ); fi
	@if ls *_assign5 >/dev/null 2>&1; then rm -rf *_assign5; fi
	@if ls *.tar.gz >/dev/null 2>&1; then rm -f *.tar.gz; fi

.PHONY: all clean submit
