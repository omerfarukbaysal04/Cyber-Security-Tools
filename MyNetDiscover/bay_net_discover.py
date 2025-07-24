import scapy.all as scapy

#Ömer Faruk Baysal|Linkedin:/baysal

#scapy.ls(scapy.ARP()) -->ARP commands

print("BAY NET DISCOVER v1.0\nGithub:@omerfarukbaysal04\n")
print("|||Process List|||\n")
print("1->Scan all devices\n2->Scan specific ip address\n3->Exit\n")

process_number=input("Please choose your process\n")
broadcast_packet=scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #-->broadcast dest

def process():
    if process_number == "1":
        arp_request_packet = scapy.ARP(pdst="10.0.2.0/24")  # -->ip request
        return arp_request_packet

    elif process_number == "2":
        target_ip = input("Enter the ip address you want to scan: ")
        arp_request_packet = scapy.ARP(pdst=target_ip)  # -->target_ip for request
        return arp_request_packet

    elif process_number == "3":
        print("Exiting...")
        exit()

    else :
        print("Invalid Input")
        exit()


def result():
    arp_request_packet=process()
    combined_packet = broadcast_packet / arp_request_packet  # -->combine broadcast and request
    print("\nScanning...\n")
    (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)  # -->lists the result
    answered_list.summary()

result()


