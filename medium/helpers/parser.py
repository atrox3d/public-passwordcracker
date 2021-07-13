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
        required=True
    )
    parser.add_argument(
        '-f',
        '--file',
        metavar='',
        type=str,
        help='keywords list ...',
        required=True
    )
    print()
    return parser
