DIR *d = opendir(name);
int dd = dirfd(d);
struct dirent *entry;

while ((entry = getNext(d)) != NULL) {
    struct stat sb;
    struct statfs dsb;
    fstatat(dd, entry->d_name, &sb, AT_SYMLINK_NOFOLLOW);
    // get metadata of directory entry

    if (S_ISREG(sb.st_mode) &&
        ((sb.st_uid == 0) && (sb.st_mode & S_ISUID)) ||
        ((sb.st_gid == 0) && (sb.st_mode & S_ISGID))) {
        // if it's a regular file and
        // the user is root & SUID is set or
        // the group is root & SGID is set

        fstatfs(dd, &dsb);
        if (!(dsb.f_flags & (ST_NOEXEC|ST_NOSUID))) {
            // get metadata of file system
            // if neither NOEXEC nor NOSUID are set
            // then this is potentially dangerous
        }
    }
}
/*
DIR *d = opendir(name);: 디렉토리를 열고 디렉토리 스트림을 반환합니다.
int dd = dirfd(d);: 디렉토리 스트림의 파일 디스크립터를 반환합니다.
struct dirent *entry;: 디렉토리 엔트리를 저장할 구조체 포인터입니다.
while ((entry = getNext(d)) != NULL): 디렉토리의 각 엔트리를 순회합니다.
struct stat sb;: 파일 상태 정보를 저장할 구조체입니다.
struct statfs dsb;: 파일 시스템 상태 정보를 저장할 구조체입니다.

fstatat(dd, entry->d_name, &sb, AT_SYMLINK_NOFOLLOW);: 디렉토리 엔트리의 메타데이터를 가져옵니다.

if (S_ISREG(sb.st_mode) && ((sb.st_uid == 0) && (sb.st_mode & S_ISUID)) 
|| ((sb.st_gid == 0) && (sb.st_mode & S_ISGID))): 
정규 파일이고, 소유자가 root이며 SUID가 설정되었거나, 그룹이 root이며 SGID가 설정된 경우를 확인합니다.

fstatfs(dd, &dsb);: 파일 시스템의 메타데이터를 가져옵니다.

if (!(dsb.f_flags & (ST_NOEXEC|ST_NOSUID))): 
파일 시스템에 NOEXEC 또는 NOSUID 플래그가 설정되지 않은 경우를 확인합니다.
*/