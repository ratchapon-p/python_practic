#!/usr/bin/env python

import subprocess
import optparse
import re

def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change it's mac address")
    parser.add_option("-m", "--mac", dest="mac_address", help="new mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please provide an interface,use --help for more information")
    if not options.mac_address:
        parser.error("[-] Please provide mac address,use --help for more information")
    return options
def change_mac(interface, mac_address):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] No mac address found")

options = get_argument()
current_mac = get_current_mac(options.interface)
print("Current mac = " + str(current_mac))
change_mac(options.interface, options.mac_address)
current_mac = get_current_mac(options.interface)
if current_mac == options.mac_address:
    print("MAC address was changed to : " + current_mac)
else:
    print("MAC address not get changed")
