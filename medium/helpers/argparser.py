import argparse
import string

# from _cffi_backend import string


def get_argument_parser():
    # Argument Parser for making cmd interative
    parser = argparse.ArgumentParser(description='arg parser')
    # adding arguments
    parser.add_argument(
        '-all',
        '--all',
        default=False,
        action='store_true',
        help='loop throug all available networks',
        required=False
    )
    parser.add_argument(
        '-ssid',
        '--ssid',
        metavar='',
        type=str,
        help='SSID = WIFI Name..',
        # required=True
    )
    parser.add_argument(
        '-passwordfile',
        '--passwordfile',
        metavar='',
        type=str,
        help='keywords list ...',
        required=True
    )
    parser.add_argument(
        '-frompassword',
        '--frompassword',
        default="",
        metavar='',
        type=str,
        help='begin from password',
        required=False
    )
    parser.add_argument(
        '-topassword',
        '--topassword',
        default=max(string.ascii_letters + string.digits + string.punctuation + string.whitespace) * 100,
        metavar='',
        type=str,
        help='end with password',
        required=False
    )
    parser.add_argument(
        '-outputfile',
        '--outputfile',
        metavar='',
        type=str,
        help='output cracked wifis ...',
        default="cracked.txt",
        required=False
    )
    parser.add_argument(
        '-verbose',
        '--verbose',
        default=False,
        action='store_true',
        help='verbose',
        required=False
    )
    print()
    return parser


