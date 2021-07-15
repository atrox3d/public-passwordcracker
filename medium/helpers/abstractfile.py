import urllib.request

from medium.helpers.constants import DARK_GREEN, RED
from sshfile import parse_ssh, ssh_file, Action


def get_filehandle(path):
    print(DARK_GREEN)
    try:
        # ssh://***REMOVED***,***REMOVED***@192.168.1.20/home/***REMOVED***/code/python/hacking/passwordcracker/brutefile.txt
        kwargs = parse_ssh(path)
        file = ssh_file(**kwargs, onexception=Action.RAISE)
        print(f"ssh: {path} is open")
    except:
        try:
            #  https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/xato-net-10-million-passwords.txt
            file = urllib.request.urlopen(path)
            print(f"urllib: {path} is open")
        except:
            print(f"urllib cannot open {path}")
            try:
                file = open(path, 'r', encoding='utf8')
                print(f"open: {path} is open")
            except:
                print(RED)
                print(f"cannot open {path}")
                exit()
    return file
