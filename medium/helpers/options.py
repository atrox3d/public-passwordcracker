import getopt
import sys


def show_help():
    # options_string = " ".join([f"[-{option}]" for option in options if option != ":"])
    print(
        f"syntax: {sys.argv[0]}\n"
        f"[-h]                     : display help and exit\n"
        f"[-a algorythm]           : algorythm (default md5)\n"
        f"[-f path or url plain]   : plain passwords file path or url\n"
        f"[-F path or url hashed]  : hashed passwords file path or url\n"
        f"[-p plain password]      : plain password to crack\n"
        f"[-P hashed password]     : hashed password to crack\n"
    )


class Options:
    # def __init__(self, options):
    #     for option in options:
    #         if option != ":":
    #             setattr(self, option, None)
    pass


def parse_options(options: str, helpopts='hH', helpfn=show_help, arguments=sys.argv[1:]):
    try:
        opts, args = getopt.getopt(
            arguments,
            options
        )
        print(f"GETOPT| {opts=}")
        print(f"GETOPT| {args=}")
    except getopt.GetoptError as goe:
        print(repr(goe))
        exit(1)

    parsed = Options()
    print(parsed.__dict__)

    for opt, arg in opts:
        if opt in [f"-{h}" for h in helpopts]:
            helpfn()
            exit()
        else:
            setattr(parsed, opt[1:], arg if arg else None)

    print(parsed.__dict__)
    return parsed


if __name__ == '__main__':
    fake_arguments = "-f hello -x".split()
    if len(sys.argv) == 1:
        arguments = fake_arguments
    else:
        arguments = sys.argv[1:]
    res = parse_options("hf:x", arguments=arguments)
    print(res.f)
