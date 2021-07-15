import argparse


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


