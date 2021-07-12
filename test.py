import sys
import time
from enum import Enum
from dataclasses import dataclass

import pywifi
import logging


class Status(Enum):
    # Define interface status.
    disconnected = pywifi.const.IFACE_DISCONNECTED
    scanning = pywifi.const.IFACE_SCANNING
    inactive = pywifi.const.IFACE_INACTIVE
    connecting = pywifi.const.IFACE_CONNECTING
    connected = pywifi.const.IFACE_CONNECTED

    @classmethod
    def getname(cls, n):
        return cls(n).name


# print(Status.getname(0))
# exit()

class Algorythms(Enum):
    # Define auth algorithms.
    open = pywifi.const.AUTH_ALG_OPEN
    shared = pywifi.const.AUTH_ALG_SHARED

    @classmethod
    def getname(cls, n):
        return cls(n).name


class Protection(Enum):
    # Define auth key mgmt types.
    none = pywifi.const.AKM_TYPE_NONE
    wpa = pywifi.const.AKM_TYPE_WPA
    wpapsk = pywifi.const.AKM_TYPE_WPAPSK
    wpa2 = pywifi.const.AKM_TYPE_WPA2
    wpa2psk = pywifi.const.AKM_TYPE_WPA2PSK
    unknown = pywifi.const.AKM_TYPE_UNKNOWN

    @classmethod
    def getname(cls, n):
        return cls(n).name


class Ciphers(Enum):
    # Define ciphers.
    none = pywifi.const.CIPHER_TYPE_NONE
    wep = pywifi.const.CIPHER_TYPE_WEP
    tkip = pywifi.const.CIPHER_TYPE_TKIP
    ccmp = pywifi.const.CIPHER_TYPE_CCMP
    unknown = pywifi.const.CIPHER_TYPE_UNKNOWN

    @classmethod
    def getname(cls, n):
        return cls(n).name


class Keys(Enum):
    networkkey = pywifi.const.KEY_TYPE_NETWORKKEY
    passphrase = pywifi.const.KEY_TYPE_PASSPHRASE

    @classmethod
    def getname(cls, n):
        return cls(n).name


@dataclass
class Profile:
    id: int
    auth: int
    akm: list
    cipher: int
    ssid: str
    bssid: str
    key: str


def show_profile(profile, name=""):
    print("*" * 80)
    print("name  : ", name)
    print("id    : ", profile.id)
    print("auth  : ", Algorythms.getname(profile.auth))
    print("akm   : ", list(map(Protection.getname, profile.akm)))
    print("cipher: ", Ciphers.getname(profile.cipher))
    print("ssid  : ", profile.ssid)
    print("bssid : ", profile.bssid)
    print("key   : ", profile.key)
    print("*" * 80)


def show_profiles():
    np = iface.network_profiles()
    print(f"show profiles: {np}")
    for p in np:
        print(vars(p))
        profile = Profile(**vars(p))
        show_profile(profile)
    print()


logging.basicConfig(
    level=logging.NOTSET,
    force=True,
    format="",
    stream=sys.stdout
)

rootlogger = logging.getLogger()
# print(f"{rootlogger.level=}")
# rootlogger.setLevel(logging.NOTSET)
logger = logging.getLogger(__name__)
#
# logging.getLogger("pywifi").addHandler(
#     logging.StreamHandler()
# )
# logging.getLogger("pywifi").setLevel(logging.NOTSET)
#
# logger.setLevel(logging.NOTSET)
logger.info("START")
# logger.error("START")
rootlogger.info("STAAART")
# exit()

w = pywifi.PyWiFi()
iface = w.interfaces()[0]

print(f"inteface: {iface.name()}")

status = iface.status()
# print(Status[status])
print(f"status: {Status(status).name}")

iface.scan()
r = iface.scan_results()
print(f"scan results: {r}")

fastweb = pywifi.Profile()

# fastweb.id = 1
fastweb.auth = Algorythms.open.value
fastweb.akm = [Protection.wpa2psk.value]
fastweb.cipher = Ciphers.ccmp.value
fastweb.ssid = "***REMOVED***"
fastweb.bssid = None
fastweb.key = "***REMOVED***"

iface.remove_all_network_profiles()
show_profiles()
show_profile(fastweb, "fastweb")

addprofile = iface.add_network_profile(fastweb)
show_profiles()
show_profile(addprofile, "addproprofile")
iface.disconnect()
iface.connect(addprofile)

time.sleep(5)
print(Status.getname(iface.status()))
print(iface.status())

exit()
