import time

from pywifi import PyWiFi

from const import PLUS, ERROR, MINUS


def initwifi():
    try:
        print(PLUS, "Initializing PyWifi:")
        # Interface information
        wifi = PyWiFi()

        print(PLUS, "getting interfaces...")
        ifaces = wifi.interfaces()
        lifaces = len(ifaces)
        if not lifaces:
            raise SystemError(f"{ERROR} no interfaces found, terminating")
        else:
            print(PLUS, f"found {len(ifaces)} interface(s)")
            for i, iface in enumerate(ifaces):
                print(f"\t{i} - {iface.name()}")
            iface = ifaces[0]  # for wifi we use index - 0
            print(PLUS, f"using 0 - {iface.name()}")

        print(PLUS, "Scannig available networks", end="")
        iface.scan()  # check the card
        wait = 5
        for t in range(wait):
            time.sleep(1)
            print(".", end="")
        print()
        # Obtain the results of the previous triggerred scan. A Profile list will be returned.
        results = iface.scan_results()
        print(f"scan found {len(results)} networks")
        for i, result in enumerate(results):
            print(f"\t{i} - {result.ssid}")

        # for result in results:
        #     for var in vars(result):
        #         print(f"{var:15}: {getattr(result, var)}")
        print(PLUS, "Init ok")
        return iface
    except Exception as e:
        print(MINUS, "Init FAIL, Error system")
        print(repr(e))
        exit()