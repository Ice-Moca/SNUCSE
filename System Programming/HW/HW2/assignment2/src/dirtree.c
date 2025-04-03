//--------------------------------------------------------------------------------------------------
// System Programming                         I/O Lab                                    Spring 2025
//
/// @file
/// @brief resursively traverse directory tree and list all entries
/// @author <yourname>
/// @studid <studentid>
//--------------------------------------------------------------------------------------------------

#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <dirent.h>
#include <errno.h>
#include <unistd.h>
#include <stdarg.h>
#include <assert.h>
#include <grp.h>
#include <pwd.h>

#define MAX_DIR 64            ///< maximum number of supported directories

/// @brief output control flags
#define F_TREE      0x1       ///< enable tree view
#define F_SUMMARY   0x2       ///< enable summary
#define F_VERBOSE   0x4       ///< turn on verbose mode

/// @brief struct holding the summary
struct summary {
  unsigned int dirs;          ///< number of directories encountered
  unsigned int files;         ///< number of files
  unsigned int links;         ///< number of links
  unsigned int fifos;         ///< number of pipes
  unsigned int socks;         ///< number of sockets

  unsigned long long size;    ///< total size (in bytes)
  unsigned long long blocks;  ///< total number of blocks (512 byte blocks)
};


/// @brief abort the program with EXIT_FAILURE and an optional error message
///
/// @param msg optional error message or NULL
void panic(const char *msg)
{
  if (msg) fprintf(stderr, "%s\n", msg);
  exit(EXIT_FAILURE);
}


/// @brief read next directory entry from open directory 'dir'. Ignores '.' and '..' entries
///
/// @param dir open DIR* stream
/// @retval entry on success
/// @retval NULL on error or if there are no more entries
struct dirent *getNext(DIR *dir)
{
  struct dirent *next;
  int ignore;

  do {
    errno = 0;
    next = readdir(dir);
    if (errno != 0) perror(NULL);
    ignore = next && ((strcmp(next->d_name, ".") == 0) || (strcmp(next->d_name, "..") == 0));
  } while (next && ignore);

  return next;
}


/// @brief qsort comparator to sort directory entries. Sorted by name, directories first.
///
/// @param a pointer to first entry
/// @param b pointer to second entry
/// @retval -1 if a<b
/// @retval 0  if a==b
/// @retval 1  if a>b
static int dirent_compare(const void *a, const void *b)
{
  struct dirent *e1 = (struct dirent*)a;
  struct dirent *e2 = (struct dirent*)b;

  // if one of the entries is a directory, it comes first
  if (e1->d_type != e2->d_type) {
    if (e1->d_type == DT_DIR) return -1;
    if (e2->d_type == DT_DIR) return 1;
  }

  // otherwise sorty by name
  return strcmp(e1->d_name, e2->d_name);
}


/// @brief recursively process directory @a dn and print its tree
///
/// @param dn absolute or relative path string
/// @param pstr prefix string printed in front of each entry
/// @param stats pointer to statistics
/// @param flags output control flags (F_*)
void processDir(const char *dn, const char *pstr, struct summary *stats, unsigned int flags)
{
// TODO
  errno = 0;
  DIR *dirStream = opendir(dn);
  if (!dirStream) {
    if (errno == EACCES) {
      printf("%sERROR: Permission denied\n", pstr);
    } else if (errno == ENOENT) {
      printf("%sERROR: File not found\n", pstr);
    }
    return;
  }

  struct dirent *entries = (struct dirent *)malloc(sizeof(struct dirent) * 1000000);
  int entryCount = 0;
  struct dirent *currentEntry;

  while ((currentEntry = getNext(dirStream)) != NULL) {
    if (!(flags & F_TREE) || currentEntry->d_type == DT_DIR) {
      entries[entryCount++] = *currentEntry;
    }
  }

  qsort(entries, entryCount, sizeof(struct dirent), dirent_compare);

  for (int i = 0; i < entryCount; i++) {
    char *filePath = (char *)malloc(strlen(dn) + strlen(entries[i].d_name) + 2);
    sprintf(filePath, "%s/%s", dn, entries[i].d_name);

    if (flags & F_SUMMARY) {
      switch (entries[i].d_type) {
        case DT_DIR: stats->dirs++; break;
        case DT_SOCK: stats->socks++; break;
        case DT_FIFO: stats->fifos++; break;
        case DT_LNK: stats->links++; break;
        case DT_REG: stats->files++; break;
      }
      struct stat fileStat;
      if (lstat(filePath, &fileStat) == 0) {
        stats->size += fileStat.st_size;
        stats->blocks += fileStat.st_blocks; // Ensure block count is added
      }
    }

    if (flags & F_VERBOSE) {
      // verbose mode output
      char *cutFileName = (char *)malloc(strlen(pstr) + strlen(entries[i].d_name) + 1);
      sprintf(cutFileName, "%s%s", pstr, entries[i].d_name);
      if (strlen(cutFileName) > 54) {
        cutFileName[53] = cutFileName[52] = cutFileName[51] = '.';
        cutFileName[54] = '\0';
      }
      printf("%-56.56s", cutFileName);
      struct stat *currentStat = (struct stat *)malloc(sizeof(struct stat));
      if (lstat(filePath, currentStat) < 0) { // get metadata
        // display error if lstat failed
        switch (errno) {
        case EACCES:
          printf("Permission denied\n");
          break;
        case ENOENT:
          printf("File not found\n");
          break;
        }
      } else {
        struct passwd *pwd;
        struct group *grp;
        if (((pwd = getpwuid(currentStat->st_uid)) != NULL) &&
            ((grp = getgrgid(currentStat->st_gid)) != NULL)) {
          printf("%-8.8s:%-8.8s  ", pwd->pw_name, grp->gr_name);
        } else {
          printf("Permission denied\n");
          continue;
        }
        printf("%*ld ", 10, currentStat->st_size);
        printf("%*ld ", 8, currentStat->st_blocks);

        switch (entries[i].d_type) {
          case DT_DIR: printf("d"); break;
          case DT_SOCK: printf("s"); break;
          case DT_FIFO: printf("f"); break;
          case DT_LNK: printf("l"); break;
          case DT_BLK: printf("b"); break;
          case DT_CHR: printf("c"); break;
          default: printf(" ");
        }
        printf("\n");
      }
      free(cutFileName);
    } else {
      printf("%s%s\n", pstr, entries[i].d_name);
    }

    if (entries[i].d_type == DT_DIR) {
      char *newPrefix = (char *)malloc(strlen(pstr) + 3);
      sprintf(newPrefix, "%s  ", pstr);
      processDir(filePath, newPrefix, stats, flags);
      free(newPrefix);
    }

    free(filePath);
  }

  free(entries);
  closedir(dirStream);
}


/// @brief print program syntax and an optional error message. Aborts the program with EXIT_FAILURE
///
/// @param argv0 command line argument 0 (executable)
/// @param error optional error (format) string (printf format) or NULL
/// @param ... parameter to the error format string
void syntax(const char *argv0, const char *error, ...)
{
  if (error) {
    va_list ap;

    va_start(ap, error);
    vfprintf(stderr, error, ap);
    va_end(ap);

    printf("\n\n");
  }

  assert(argv0 != NULL);

  fprintf(stderr, "Usage %s [-t] [-s] [-v] [-h] [path...]\n"
                  "Gather information about directory trees. If no path is given, the current directory\n"
                  "is analyzed.\n"
                  "\n"
                  "Options:\n"
                  " -t        print the directory tree (default if no other option specified)\n"
                  " -s        print summary of directories (total number of files, total file size, etc)\n"
                  " -v        print detailed information for each file. Turns on tree view.\n"
                  " -h        print this help\n"
                  " path...   list of space-separated paths (max %d). Default is the current directory.\n",
                  basename(argv0), MAX_DIR);

  exit(EXIT_FAILURE);
}


/// @brief program entry point
int main(int argc, char *argv[])
{
  //
  // default directory is the current directory (".")
  //
  const char CURDIR[] = ".";
  const char *directories[MAX_DIR];
  int   ndir = 0;

  struct summary tstat;
  unsigned int flags = 0;

  //
  // parse arguments
  //
  for (int i = 1; i < argc; i++) {
    if (argv[i][0] == '-') {
      // format: "-<flag>"
      if      (!strcmp(argv[i], "-t")) flags |= F_TREE;
      else if (!strcmp(argv[i], "-s")) flags |= F_SUMMARY;
      else if (!strcmp(argv[i], "-v")) flags |= F_VERBOSE;
      else if (!strcmp(argv[i], "-h")) syntax(argv[0], NULL);
      else syntax(argv[0], "Unrecognized option '%s'.", argv[i]);
    } else {
      // anything else is recognized as a directory
      if (ndir < MAX_DIR) {
        directories[ndir++] = argv[i];
      } else {
        printf("Warning: maximum number of directories exceeded, ignoring '%s'.\n", argv[i]);
      }
    }
  }

  // if no directory was specified, use the current directory
  if (ndir == 0) directories[ndir++] = CURDIR;


  //
  // process each directory
  //
  // TODO
  // Pseudo-code
  // - reset statistics (tstat)
  // - loop over all entries in 'directories' (number of entires stored in 'ndir')
  //   - reset statistics (dstat)
  //   - if F_SUMMARY flag set: print header
  //   - print directory name
  //   - call processDir() for the directory
  //   - if F_SUMMARY flag set: print summary & update statistics

  // reset statistics (tstat)
  memset(&tstat, 0, sizeof(tstat));
  // loop over all entries in 'directories' (number of entires stored in 'ndir')
  for (int dirIndex = 0; dirIndex < ndir; dirIndex++) {
    struct summary dirStats;
    // reset statistics (dstat)
    memset(&dirStats, 0, sizeof(dirStats));

    // if summary flag set : print header
    if (flags & F_SUMMARY) {
      printf("Name\n");
      if (flags & F_VERBOSE) {
        printf("Name                                                        "
              "User:Group           Size    Blocks Type\n");
      }
      printf("-----------------------------------------------------------------"
            "-----------------------------------\n");
    }

    // print directory name
    printf("%s\n", directories[dirIndex]);
    // call processDir() for the director
    processDir(directories[dirIndex], "", &dirStats, flags);

    // if F_SUMMARY flag set: print summary & update statistics
    if (flags & F_SUMMARY) {
      tstat.dirs += dirStats.dirs;
      tstat.files += dirStats.files;
      tstat.links += dirStats.links;
      tstat.fifos += dirStats.fifos;
      tstat.socks += dirStats.socks;
      tstat.size += dirStats.size;
      tstat.blocks += dirStats.blocks;

      printf("-----------------------------------------------------------------"
            "-----------------------------------\n");

      // Print directory summary
      if (flags & F_TREE) {
        printf("%d %s\n", dirStats.dirs, dirStats.dirs == 1 ? "directory" : "directories");
      } 
      else {
        char summaryBuffer[500] = {0};
        snprintf(summaryBuffer, sizeof(summaryBuffer), "%d %s, %d %s, %d %s, %d %s, and %d %s",
                dirStats.files, dirStats.files == 1 ? "file" : "files",
                dirStats.dirs, dirStats.dirs == 1 ? "directory" : "directories",
                dirStats.links, dirStats.links == 1 ? "link" : "links",
                dirStats.fifos, dirStats.fifos == 1 ? "pipe" : "pipes",
                dirStats.socks, dirStats.socks == 1 ? "socket" : "sockets");

        if (flags & F_VERBOSE) {
          printf("%-68.68s   %14llu %8llu\n", summaryBuffer, dirStats.size, dirStats.blocks);
        } else {
          printf("%s\n", summaryBuffer);
        }
      }
      printf("\n");
    }
  }

  //
  // print grand total
  //
  if ((flags & F_SUMMARY) && (ndir > 1)) {
    printf("Analyzed %d directories:\n"
           "  total # of files:        %16d\n"
           "  total # of directories:  %16d\n"
           "  total # of links:        %16d\n"
           "  total # of pipes:        %16d\n"
           "  total # of sockets:      %16d\n",
           ndir, tstat.files, tstat.dirs, tstat.links, tstat.fifos, tstat.socks);

    if (flags & F_VERBOSE) {
      printf("  total file size:         %16llu\n"
             "  total # of blocks:       %16llu\n",
             tstat.size, tstat.blocks);
    }

  }

  //
  // that's all, folks!
  //
  return EXIT_SUCCESS;
}

