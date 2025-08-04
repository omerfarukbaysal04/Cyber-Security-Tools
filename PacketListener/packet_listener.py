import scapy.all as scapy
from scapy.layers import http

def listen_packets(interface):
    scapy.sniff(iface=interface,store=False,prn=analyze_packets)
    #prn -> callback func -- store ->save data to memory ?

def analyze_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet.getlayer(scapy.Raw).load)
    #packet.show() ->shows all packets

listen_packets("eth0")