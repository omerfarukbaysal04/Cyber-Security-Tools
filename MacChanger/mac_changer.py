import subprocess
import argparse
import re

print("|MAC CHANGER v1.1|\n")
print("GitHub:@omerfarukbaysal04")
print("------------------")

def get_user_inputs():
    parse_object = argparse.ArgumentParser()
    parse_object.add_argument("-i", "--interface", dest="interface",help="interface to change!",required=True)  # -i ->short name ve --interface -> long name
    parse_object.add_argument("-m", "--mac", dest="mac_address", help="new mac address!",required=True)  # -m ->short name ve --mac -> long name

    return parse_object.parse_args()

def change_mac_address(user_interface,user_mac_address):
    subprocess.call(["ifconfig", user_interface,"down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])

def control_new_mac(interface):

    ifconfig=subprocess.check_output((["ifconfig",interface]))
    new_mac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))

    if new_mac:
        return new_mac.group(0)
    else:
        return None

user_input=get_user_inputs()

change_interface=user_input.interface
change_mac=user_input.mac_address

change_mac_address(change_interface, change_mac)

finalized_mac_address=control_new_mac(change_interface)

print("Mac changing started!")
print("------------------")

if finalized_mac_address==user_input.mac_address:
    print("Mac address changed successfully!")
else:
    print("Something went wrong ):")

