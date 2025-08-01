# Hands-on Linux-03 : Managing Users and Groups


## Outline

- Part 1 - Basic User Commands

- Part 2 - User Management

- Part 3 - User Passwords

- Part 4 - Group Management

## Part 1 - Basic User Commands
​
- `whoami` command
​
```bash
whoami
sudo su
pwd
whoami
su ec2-user
sudo su -
pwd
```
​
- `who` command
​
```bash
exit
who
who # open a new shell and retry who command to see the users who logged in.
```
​
- `w` command
​
```bash
w
who
```
​
- `id` command
​
```bash
id
id root
sudo su
useradd Greg
id Greg
```
​
- `su` command
​
```bash
su ec2-user
su Greg
sudo su Greg
pwd
exit
sudo su - Greg
pwd
```
​
- `passwd` command
​
```bash
exit
sudo su
useradd ferguson
passwd ferguson    # give a password to ferguson
su - ferguson
passwd
exit
su ferguson
```
​
## Part 2 - User management
​
- /etc/passwd.
​
```bash
exit
cat /etc/passwd
tail -3 /etc/passwd
```
​
- `useradd` command
​
```bash
sudo useradd meryem
cd /home
ls
cd /etc
ls login*
cat login.defs
sudo nano login.defs    # change the CREATE_HOME variable's value to "no"
sudo useradd jack
cd /home && ls
cat /etc/passwd
sudo useradd -m nixon    # force to system to create a home directory for user with -m option.
cd /home && ls
sudo useradd -m -d /home/johnhome john    # change the user's home directory name with -d option.
ls
sudo useradd -m -c "new commer" alex    # give a descrpition to user with -c option.
cat /etc/passwd
cat /etc/passwd | grep alex
```
​
- userdel.
​
```bash
cat /etc/passwd
sudo userdel nixon
cat /etc/passwd
cd /home && ls
sudo userdel -r Greg    # delete user and its home directory with -r option.
cd /home && ls
```
​
- usermod.
​
```bash
cat /etc/passwd
sudo usermod -c "new manager" alex
cat /etc/passwd
sudo usermod --help
sudo usermod -l Superuser ferguson    # change the name of the ferguson with -l option.
cat /etc/passwd
```
​
## Part 3 - User Passwords
​
- passwd-etc/shadow-etc/login.defs.
​
```bash
  sudo su
  useradd user8
  passwd user8
  cd /etc
  cat shadow
  cat login.defs
```
​
## Part 4 - Group Management
​
- groups.
​
```bash
groups
sudo groupadd linux
sudo groupadd aws
sudo groupadd python
cat /etc/group
groups
sudo usermod -a -G linux ec2-user    # append ec2-user in linux group.
cat /etc/group
groups
sudo usermod -G aws ec2-user    # this command deletes all groups that ec2-user in except default group of ec2-user and add ec2-user to aws group.
cat /etc/group
sudo groupmod -n my-linux linux    # change the name of the linux group.
cat /etc/group
groups
cat /etc/group
sudo groupdel python
cat /etc/group
sudo gpasswd -a alex aws    # add a user to a group.
cat /etc/group
sudo gpasswd -d alex aws    # delete a user to a group.
cat /etc/group
```