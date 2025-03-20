#include <grp.h>
#include <pwd.h>

int main(int argc, char *argv[]) {
    // get user id, effective user id, group id, effective group id
    uid_t uid = getuid();
    uid_t euid = geteuid();
    gid_t gid = getgid();
    gid_t egid = getegid();

    // get user and group names
    char *user, *euser, *group, *egroup;
    struct passwd *pwd;
    struct group *grp;

    if ((pwd = getpwuid(uid)) != NULL) user = strdup(pwd->pw_name);
    if ((pwd = getpwuid(euid)) != NULL) euser = strdup(pwd->pw_name);
    if ((grp = getgrgid(gid)) != NULL) group = strdup(grp->gr_name);
    if ((grp = getgrgid(egid)) != NULL) egroup = strdup(grp->gr_name);

    // print results
    printf("User & group information\n"
        "-------------------------\n"
        " User: %-16s (%d)\n"
        " Group: %-16s (%d)\n"
        "\n"
        " Effective user: %-16s (%d)\n"
        " Effective group: %-16s (%d)\n",
        user ? user : "n/a", uid,
        group ? group : "n/a", gid,
        euser ? euser : "n/a", euid,
        egroup ? egroup : "n/a", egid);

    // free allocated memory
    free(user); free(euser); free(group); free(egroup);

    return EXIT_SUCCESS;
}

/*
#include <grp.h>: 그룹 관련 함수와 구조체를 포함합니다.
#include <pwd.h>: 사용자 관련 함수와 구조체를 포함합니다.
uid_t uid = getuid();: 실제 사용자 ID를 가져옵니다.
uid_t euid = geteuid();: 유효 사용자 ID를 가져옵니다.
gid_t gid = getgid();: 실제 그룹 ID를 가져옵니다.
gid_t egid = getegid();: 유효 그룹 ID를 가져옵니다.
if ((pwd = getpwuid(uid)) != NULL) user = strdup(pwd->pw_name);: 실제 사용자 이름을 가져옵니다.
if ((pwd = getpwuid(euid)) != NULL) euser = strdup(pwd->pw_name);: 유효 사용자 이름을 가져옵니다.
if ((grp = getgrgid(gid)) != NULL) group = strdup(grp->gr_name);: 실제 그룹 이름을 가져옵니다.
if ((grp = getgrgid(egid)) != NULL) egroup = strdup(grp->gr_name);: 유효 그룹 이름을 가져옵니다.
printf(...): 사용자 및 그룹 정보를 출력합니다.
free(user); free(euser); free(group); free(egroup);: 할당된 메모리를 해제합니다.
*/