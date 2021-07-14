####################################################################################################################
'''
You can Read about every single detail in depth on https://rsajal.medium.com
Link to Github - https://github.com/r-sajal/Ethical-Hacking
'''
####################################################################################################################

# important libraries
import itertools  # efficient looping
import string  # string functions
import sys
import time  # time checking
import os

from helpers import options


def password_wordlist(start_range=8, end_range=10, file_name="brute.txt"):
    # string with all characters needed or have potential for being password
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + '@' + '#' + '$' + '.'
    # attempts counter
    attempts = 0
    # open file
    f = open(file_name, 'a')

    for password_length in range(start_range, end_range):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            f.write(guess)  # write in file
            f.write("\n")
            print(f"{guess:{end_range+1}}: {attempts:20,}")

    # close file
    f.close()


def show_help():
    print(os.path.basename(sys.argv[0]), "-h -s start -e end -f filename")


if __name__ == '__main__':
    #
    #   parse command line options
    #
    opts = options.parse_options("hs:e:f:", help_function=show_help)
    #
    #   check mandatory arguments
    #
    if not all((opts.s, opts.e, opts.f)):
        show_help()
        exit()
    #
    #   init variables
    #
    start_range = int(opts.s)
    end_range = int(opts.e)
    file_name = opts.f
    start_time = time.time()
    start_timef = time.strftime("%Y%m%d-%H:%M:%S", time.localtime(start_time))
    print(f"{start_range = }")
    print(f"{end_range   = }")
    print(f"{file_name   = }")
    print(f"{start_timef = }")
    # Main function Call
    password_wordlist(start_range, end_range, file_name)

    end_time = time.time()
    end_timef = time.strftime("%Y%m%d-%H:%M:%S", time.localtime(end_time))
    timediff = end_time - start_time
    print(f"{start_range = }")
    print(f"{end_range   = }")
    print(f"{file_name   = }")
    print(f"{end_timef   = }")
    print(f"{timediff    = }")


    ##### Code by Sajal Rastogi
