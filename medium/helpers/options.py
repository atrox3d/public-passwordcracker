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
    def __init__(self, options):
        for option in options:
            if option != ":":
                setattr(self, option, None)
    # pass


def parse_options(
        option_string: str,  # getopt options: "hf:x"
        help_options='hH',  # help options: -h, -H
        help_function=show_help,  # help/syntax function
        parameters=sys.argv[1:]  # actual parameters
):
    try:
        #
        #   parse parameters
        #
        options, arguments = getopt.getopt(
            parameters,
            option_string
        )
        print(f"GETOPT| {options=}")
        print(f"GETOPT| {arguments=}")
    except getopt.GetoptError as goe:
        print(repr(goe))
        exit(1)
    #
    #   create option result object
    #
    parsed_options = Options(option_string)
    #
    #   loop though tuples ('-f', 'filename')
    #
    for option, option_arg in options:
        #
        #   search in dynamically created help options list [ '-h', '-H' ]
        #
        if option in [f"-{help_option}" for help_option in help_options]:
            help_function()  # call help if match
            exit()
        else:
            #
            #   populate result object
            #
            setattr(
                parsed_options,
                option[1:],  # remove dash
                option_arg if option_arg else None
            )
        # expected_parameters = options.count(':')

    # print(parsed.__dict__)
    return parsed_options


if __name__ == '__main__':
    fake_arguments = "-f hello -x".split()
    if len(sys.argv) == 1:
        arguments = fake_arguments
    else:
        arguments = sys.argv[1:]
    res = parse_options("hf:x", parameters=arguments)
    print(res.f)
