import argparse
import urllib.request

from .constants import *

def get_argument_parser():
    # Argument Parser for making cmd interative
    parser = argparse.ArgumentParser(description='arg parser')
    # adding arguments
    parser.add_argument(
        '-s',
        '--ssid',
        metavar='',
        type=str,
        help='SSID = WIFI Name..',
        # required=True
    )
    parser.add_argument(
        '-f',
        '--file',
        metavar='',
        type=str,
        help='keywords list ...',
        required=True
    )
    parser.add_argument(
        '-v',
        '--verbose',
        default=False,
        action='store_true',
        help='verbose',
        required=False
    )
    parser.add_argument(
        '-a',
        '--all',
        default=False,
        action='store_true',
        help='loop throug all available networks',
        required=False
    )
    print()
    return parser


def get_filehandle(path):
    print(DARK_GREEN)
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
