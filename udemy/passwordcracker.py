import urllib.request
import hashlib

import options

DEFAULT_ALGORYTHM = 'md5'

# if len(sys.argv) < 3+1:
#     print(f"syntax {sys.argv[0]} algorythm (default md5) password-file password")
#     exit()
#
# algorythm, passwordfile, hashed_password = sys.argv[1:1 + 3]
#
# print(algorythm, passwordfile, hashed_password)

parameters = (
    algorythm,
    plain_file,
    hashed_file,
    plain_password,
    hashed_password,
    args,
) = options.parse_options()

print(
    algorythm,
    plain_file,
    hashed_file,
    plain_password,
    hashed_password,
    args,
)

if not any(parameters):
    options.show_help()
    exit()

algorythm = algorythm or DEFAULT_ALGORYTHM

if not any((plain_file, hashed_file)):
    print("ERROR| please specify a password file")
    options.show_help()
    exit()

if not any((plain_password, hashed_password)):
    print("ERROR| please specify a password ")
    options.show_help()
    exit()

if algorythm not in hashlib.algorithms_guaranteed:
    print(f"sorry, algorythm {algorythm} is not available")
    print(f"available algorythms: {hashlib.algorithms_guaranteed}")
    exit()
else:
    hasher = getattr(hashlib, algorythm)
    print(f"selected algorythm: {algorythm}: {hasher}")

print(f"{algorythm=}")
print(f"{plain_file=}")
print(f"{hashed_file=}")
print(f"{plain_password=}")
print(f"{hashed_password=}")

# try:
#     file = open(passwordfile)
#     print(file"file {passwordfile} is open for input")
# except:
#     print(file"the file {passwordfile} does not exist, exiting.")
#     exit()
passwordfile = plain_file or hashed_file
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

print(f"password to crack: {hashed_password or plain_password}")
# exit()
print("START")
# for line in file.readlines():
for line in file:
    try:
        # url
        line = line.decode('utf-8').strip().strip('\r').strip('\n')
    except:
        # file
        line = line.strip().strip('\r').strip('\n')
        pass

    if plain_file and hashed_password:
        line = hasher(line.encode()).hexdigest()
        password = hashed_password
    elif plain_file and plain_password:
        password = plain_password
        # line = line
    elif hashed_file and plain_password:
        password = hasher(plain_password.encode()).hexdigest()
        # line = line
    elif hashed_file and hashed_password:
        password = hashed_password
        # line = line

    if password == line:
        print(f"{password} - {line} : OK: {line}")
        exit()
    else:
        print(f"{password} - {line} : KO ({line})")
