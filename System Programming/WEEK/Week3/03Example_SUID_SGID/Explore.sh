# Set user/group owner
sudo chown <usr>[:<grp>]

# Set suid/sgid bit
suid bit
sudo chmod 4755 <exe>

sgid bit
sudo chmod 2755 <exe>

suid+sgid bits
sudo chmod 6755 <exe>

# Check the permissions
: '
sudo chown <usr>[:<grp>]: 파일의 소유자 및 그룹을 변경합니다.
sudo chmod 4755 <exe>: 파일에 SUID 비트를 설정합니다.
sudo chmod 2755 <exe>: 파일에 SGID 비트를 설정합니다.
sudo chmod 6755 <exe>: 파일에 SUID 및 SGID 비트를 설정합니다.
'
