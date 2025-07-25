import subprocess
import optparse
import re

print("|MAC CHANGER v1.0|\n")
print("GitHub:@omerfarukbaysal04")
print("------------------")

def get_user_inputs():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface",help="interface to change!")  # -i ->kısa ad ve --interface ->uzun ad
    parse_object.add_option("-m", "--mac", dest="mac_address", help="new mac address!")

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

(user_input,arguments)=get_user_inputs()
change_mac_address(user_input.interface,user_input.mac_address)
finalized_mac_address=control_new_mac(str(user_input.interface))

print("Mac changing started!")
print("------------------")

if finalized_mac_address==user_input.mac_address:
    print("Mac address changed successfully!")
else:
    print("Something went wrong ):")

