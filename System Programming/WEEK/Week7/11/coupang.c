#define _POSIX_C_SOURCE 200809L
#include "trim.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <termios.h>
#include <unistd.h>

// Slide 16

char *password, *encoded, *trimmed;
char *secret = "Zljyl{Whzz~vyk(";

ssize_t read_pwd(char **lineptr, size_t *n, FILE *stream) {
  struct termios old, new;
  int nread;

  // Turn echoing off and fail if we can't.
  if (tcgetattr(fileno(stream), &old) != 0)
    return -1;

  new = old;
  new.c_lflag &= ~ECHO;

  if (tcsetattr(fileno(stream), TCSAFLUSH, &new) != 0)
    return -1;

  // Read the password.
  nread = getline(lineptr, n, stream);

  // Restore terminal.
  (void)tcsetattr(fileno(stream), TCSAFLUSH, &old);

  return nread;
}
char *encode(char *password) { return password; }

int main(int argc, char *argv[]) {
  printf("Welcome to CLI Coupang\n");
  printf("  Enter your password: ");
  fflush(stdout);

  password = NULL;
  size_t pwd_len = 0;

  if (read_pwd(&password, &pwd_len, stdin) <= 0) {
    printf("\n\nCannot read password!\n");
    return EXIT_FAILURE;
  }

  encoded = encode(password);

  trimmed = trim(encoded);

  if ((trimmed == NULL) || (strcmp(trimmed, secret) != 0)) {
    printf("\n\nWrong password.\n");
    return EXIT_FAILURE;
  }

  printf("\n\nWhat would you like to buy?\n");

  return EXIT_SUCCESS;
}
