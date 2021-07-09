import getopt
import sys


def show_help():
    # options_string = " ".join([f"[-{option}]" for option in options if option != ":"])
    print(
        f"syntax: {sys.argv[0]}\n"
        f"[-h]                     : display help and exit\n"
        f"[-a algorythm]           : algorythm (default md5)\n"
        f"[-f path or url plain]   : plain passwords file path or url"
        f"[-F path or url hashed]  : hashed passwords file path or url"
        f"[-p plain password]      : plain password to crack\n"
        f"[-P hashed password]     : hashed password to crack\n"
    )


def parse_options():
    options = "ha:f:F:p:P:"

    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            options
        )
        print(f"GETOPT| {opts=}")
        print(f"GETOPT| {args=}")
    except getopt.GetoptError as goe:
        print(repr(goe))
        exit(1)

    algorythm = None
    plain_file = None
    hashed_file = None
    plain_password = None
    hashed_password = None

    for opt, arg in opts:
        if opt in ['-a']:
            algorythm = arg
            print(f"GETOPT| set algorythm to: {algorythm}")
        elif opt in ['-f']:
            plain_file = arg
            print(f"GETOPT| plain password file: {plain_file}")
        elif opt in ['-F']:
            hashed_file = arg
            print(f"GETOPT| hashed password file: {hashed_file}")
        elif opt in ['-p']:
            plain_file = arg
            print(f"GETOPT| plain password : {plain_password}")
        elif opt in ['-P']:
            hashed_password = arg
            print(f"GETOPT| hashed password : {hashed_password}")
        elif opt in ['-h']:
            show_help()
            exit()
    return (
        algorythm,
        plain_file,
        hashed_file,
        plain_password,
        hashed_password,
        args,
    )
