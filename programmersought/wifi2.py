# https://www.programmersought.com/article/48124669524/


# Try and connect to wifi
import pywifi
import time


def isConnected():
    if ifaces.status() == pywifi.const.IFACE_CONNECTED:
        print(f"iface {ifaces.name()} is connected ({ifaces.status()})")
        return True
    else:
        print(f"iface {ifaces.name()} is DISconnected ({ifaces.status()})")
        return False


if __name__ == "__main__":
    wifi = pywifi.PyWiFi()  # Create a wireless object
    ifaces = wifi.interfaces()[0]  # Take an unlimited network card
    print(ifaces.name())  # Output wireless network card name
    # print(ifaces.status())
    isConnected()

    profile = pywifi.Profile()
    print(profile)
    print([m for m in dir(profile) if not m.startswith('__')])
    exit()

    ifaces.disconnect()  # Disconnect the network card
    time.sleep(0.5)  # Buffer 0.5 seconds

    ifaces.disconnect()  # Disconnect the network card
    isConnected()

    profile = pywifi.Profile()  # Configuration file
    profile.ssid = "***REMOVED***"  # wifi name
    profile.key = "***REMOVED***"
    ifaces.remove_all_network_profiles()  # Delete other configuration files
    tmp_profile = ifaces.add_network_profile(profile)  # Load configuration file
    ifaces.connect(tmp_profile)  # Connect
    time.sleep(0.5)  # Wait for 0.5 seconds to see if the connection is successful
    if not isConnected():
        time.sleep(5)  # If unsuccessful, wait 5 seconds and then see if the connection is successful
        isConnected()
