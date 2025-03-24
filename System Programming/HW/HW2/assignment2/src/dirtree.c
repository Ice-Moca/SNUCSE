//--------------------------------------------------------------------------------------------------
// System Programming                         I/O Lab                                    Spring 2025
//
/// @file
/// @brief resursively traverse directory tree and list all entries
/// @author <EunSu Yeo>
/// @studid <202312753>
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

#define MAX_DIR 64            ///< maximum number of supported directories, directory의 최대 개수

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
  struct dirent *next;    //save entry that readdir() read
  int ignore;             //flag to check entry is '.' or '..'

  do {
    errno = 0;
    next = readdir(dir);  //if not data in dir, return NULL
    if (errno != 0) perror(NULL); //if error, print error message
    ignore = next && ((strcmp(next->d_name, ".") == 0) || (strcmp(next->d_name, "..") == 0));
    //if next is not null and d_name is . or .. set ignore 1
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
  //a,b is pointer to struct dirent
  struct dirent *e1 = (struct dirent*)a; 
  struct dirent *e2 = (struct dirent*)b;

  // if one of the entries is a directory, it comes first
  if (e1->d_type != e2->d_type) { 
    // data type=DT_DIR print that first
    // else don't care about data type
    if (e1->d_type == DT_DIR) return -1;
    if (e2->d_type == DT_DIR) return 1;
  }

  // otherwise sorty by name
  // if data type is same, sort by name
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
  //open directory
  DIR *dir = opendir(dn); 

  if(dir==NULL){ 
    //if error, print error message
    fprintf(stderr, "%s: ERROR: %s\n", dn, strerror(errno)); 
    return;
  }

  // entries: array of pointers to struct dirent
  // entry: pointer to struct dirent
  // count: number of entries read
  // capacity: number of entries that can be stored in entries
  int count=0; 
  int capacity = 16;
  struct dirent *entry;
  struct dirent **entries=NULL;
  // entries = malloc(capacity * sizeof(struct dirent*));
  // malloc: allocate memory for entries
  // need free(entries) at the end of the function
  entries = malloc(capacity * sizeof(struct dirent*));

  if(!entries){
    // if entries is null, print error message
    panic("Out of memory.");
  }

  while((entry=getNext(dir))!=NULL){
    if(count==capacity){
      capacity*=2;
      entries=realloc(entries, capacity*sizeof(struct dirent*));
      if(!entries){
        // if entries is null, print error message
        panic("Out of memory.");
      }
    }
    // save entry in entries 
    // count increase after saving entry
    entries[count++]=entry;
  }
  // finish reading directory
  closedir(dir);

  // quick sort entries by name
  // entries: array of pointers to struct dirent
  // count: number of entries
  // sizeof(struct dirent*): size of each element
  // dirent_compare: compare function
  // In qsort function dirent_compare is used to compare entries
  qsort(entries, count, sizeof(struct dirent*), dirent_compare);

  // loop over all entries
  // entries is sorted by name in here
  for (int i = 0; i < count; i++) {
    struct dirent *e = entries[i];
    char path[PATH_MAX];
    // snprintf: write formatted output to sized buffer
    snprintf(path, sizeof(path), "%s/%s", dn, e->d_name);

    struct stat st;
    // lstat: get file status
    // &st: save file metadata in st
    // if lstat fails, print error message
    if (lstat(path, &st) == -1) {
      fprintf(stderr, "%s: ERROR: %s\n", path, strerror(errno));
      continue;
    }

    // print file information
    // if VERBOSE flag is set, print detailed information
    if (flags & F_VERBOSE) {
      printf("%s%-54.54s %8s:%-8s %10lld %8lld %c\n", 
            pstr, e->d_name, 
            getpwuid(st.st_uid)->pw_name, 
            getgrgid(st.st_gid)->gr_name, 
            (long long)st.st_size, 
            (long long)st.st_blocks, 
            S_ISDIR(st.st_mode) ? 'd' : S_ISLNK(st.st_mode) ? 'l' : S_ISFIFO(st.st_mode) ? 'f' : S_ISSOCK(st.st_mode) ? 's' : ' ');
    } else {
      printf("%s%s\n", pstr, e->d_name);
    }

    // bitwise AND operation
    // S_IFMT: file type mask
    // st.st_mode contians file type in the Upper 4bits
    // reference: https://12bme.tistory.com/215 

    switch (st.st_mode & S_IFMT) {
      case S_IFDIR: // Directory case
        // if entry is directory, set stats->dirs and increase dirs
        // snprintf: write formatted output to sized buffer
        // processDir: recursively process directory with new prefix
        stats->dirs++;
        char new_prefix[PATH_MAX];
        snprintf(new_prefix, sizeof(new_prefix), "%s%s  ", pstr, (flags & F_TREE) ? "|-" : "  ");
        processDir(path, new_prefix, stats, flags);
        break;

      case S_IFREG: // Regular file case
        stats->files++;
        break;

      case S_IFLNK: // Symbolic link case
        stats->links++;
        break;

      case S_IFIFO: // FIFO case
        stats->fifos++;
        break;

      case S_IFSOCK: // Socket case
        stats->socks++;
        break;

      default:
        // error case
        break;
    }

    stats->size += st.st_size;
    stats->blocks += st.st_blocks;
  }

  //free entries
  free(entries);
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
  //
  // Pseudo-code
  // - reset statistics (tstat)
  // - loop over all entries in 'directories' (number of entires stored in 'ndir')
  //   - reset statistics (dstat)
  //   - if F_SUMMARY flag set: print header
  //   - print directory name
  //   - call processDir() for the directory
  //   - if F_SUMMARY flag set: print summary & update statistics
  memset(&tstat, 0, sizeof(tstat));
  
  for (int i = 0; i < ndir; i++) {
    struct summary dstat = {0};
    if (flags & F_SUMMARY) {
      printf("Name\n");
      printf("----------------------------------------------------------------------------------------------------\n");
    }

    printf("%s\n", directories[i]);
    processDir(directories[i], "", &dstat, flags);

    if (flags & F_SUMMARY) {
      printf("----------------------------------------------------------------------------------------------------\n");
      printf("%u files, %u directories, %u links, %u pipes, and %u sockets\n", 
            dstat.files, dstat.dirs, dstat.links, dstat.fifos, dstat.socks);
      if (flags & F_VERBOSE) {
        printf("Total size: %llu bytes, Total blocks: %llu\n", dstat.size, dstat.blocks);
      }
    }

    tstat.files += dstat.files;
    tstat.dirs += dstat.dirs;
    tstat.links += dstat.links;
    tstat.fifos += dstat.fifos;
    tstat.socks += dstat.socks;
    tstat.size += dstat.size;
    tstat.blocks += dstat.blocks;
  }
  //...


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

