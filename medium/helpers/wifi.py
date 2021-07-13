import time

from pywifi import PyWiFi

from .constants import *


class Wifi:
    # def initwifi():
    def __init__(self):
        self.wifi = None
        self.ifaces = []
        self.ifaces_count = 0
        self.networks = []
        self.networks_count = 0
        self.profiles = []
        self.profiles_count = 0

        """ initialize or die """
        try:
            print(GREEN)
            print(PLUS, "Initializing PyWifi:")
            # Interface information
            self.wifi = PyWiFi()

            self.ifaces = self.get_ifaces()
            self.iface = self.ifaces[0]  # for wifi we use index - 0
            print(GREEN)
            print(PLUS, f"using 0 - {self.iface.name()}")

            self.networks = self.scan_networks()

            print(PLUS, "Init ok")
            # return iface
        except Exception as e:
            print(MINUS, "Init FAIL, Error system")
            print(repr(e))
            exit()

    def scan_networks(self):
        print(DARK_GREEN)
        print(PLUS, "Scannig available networks", end="")
        self.iface.scan()  # check the card
        wait = 5
        for t in range(wait):
            time.sleep(1)
            print(".", end="")
        print()

        # Obtain the results of the previous triggerred scan. A Profile list will be returned.
        self.networks = self.iface.scan_results()
        if not len(self.networks):
            print(RED)
            print("No networks found, exiting")
            exit()
        else:
            self.networks_count = len(self.networks)
            print(GREEN)
            print(PLUS, f"scan found {len(self.networks)} networks")
            for i, network in enumerate(self.networks):
                print(f"\t{i} - {network.ssid}")

            return self.networks

    def get_ifaces(self):
        print(DARK_GREEN)
        print(PLUS, "getting interfaces...")
        self.ifaces = self.wifi.interfaces()
        self.ifaces_count = len(self.ifaces)
        if not self.ifaces_count:
            raise SystemError(f"{ERROR} no interfaces found, terminating")
        else:
            print(PLUS, f"found {len(self.ifaces)} interface(s)")
            for i, iface in enumerate(self.ifaces):
                print(f"\t{i} - {iface.name()}")
        return self.ifaces

