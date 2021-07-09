import urllib.request
import sys
import hashlib

DEFAULT_ALGORYTHM = 'md5'

if len(sys.argv) < 3+1:
    print(f"syntax {sys.argv[0]} algorythm (default md5) password-file password")
    exit()

algorythm, passwordfile, hashed_password = sys.argv[1:1 + 3]

print(algorythm, passwordfile, hashed_password)


if algorythm not in hashlib.algorithms_guaranteed:
    print(f"sorry, algorythm {algorythm} is not available")
    print(f"available algorythms: {hashlib.algorithms_guaranteed}")
    exit()
else:
    hasher = getattr(hashlib, algorythm)
    print(f"selected algorythm: {algorythm}: {hasher}")


# try:
#     file = open(passwordfile)
#     print(file"file {passwordfile} is open for input")
# except:
#     print(file"the file {passwordfile} does not exist, exiting.")
#     exit()
try:
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

print(f"password to crack: {hashed_password}")

print("START")
# for line in file.readlines():
for line in file:
    try:
        line = line.decode('utf-8').strip().strip('\r').strip('\n')
    except:
        line = line.strip().strip('\r').strip('\n')
        pass
    hashed_line = hasher(line.encode()).hexdigest()
    if hashed_password == hashed_line:
        print(f"{hashed_password} - {hashed_line} : OK: {line}")
        exit()
    else:
        print(f"{hashed_password} - {hashed_line} : KO ({line})")