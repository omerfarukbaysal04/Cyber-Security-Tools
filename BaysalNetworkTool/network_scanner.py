import scapy.all as scapy
import socket
from mac_vendor_lookup import MacLookup
from impacket.nmb import NetBIOS
import os
import time
from zeroconf import Zeroconf, ServiceBrowser
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox, PhotoImage

#@Github: Ömer Faruk Baysal
broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

# --- Vendor DB Auto Update ---
def auto_update_vendor():
    cache_file = os.path.expanduser("~/.mac-vendors.txt")

    if not os.path.exists(cache_file) or (time.time() - os.path.getmtime(cache_file)) > 7 * 24 * 3600:
        print("🔄 Updating vendor database (weekly check)...")
        try:
            MacLookup().update_vendors()
            print("✅ Vendor database updated!")
        except Exception as e:
            print(f"❌ Update failed: {e}")

# --- Hostname Detection ---
def get_hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        if hostname != ip:
            return hostname
    except socket.herror:
        pass

    try:
        bios = NetBIOS()
        names = bios.queryIPForName(ip, timeout=2)
        bios.close()
        if names:
            return names[0]
    except Exception:
        pass

    try:
        hostname = mdns_lookup(ip)
        if hostname:
            return hostname
    except Exception:
        pass

    return "Unknown"

# --- mDNS Lookup ---
def mdns_lookup(ip):
    result = []

    class Listener:
        def remove_service(self, zeroconf, type, name):
            pass

        def add_service(self, zeroconf, type, name):
            info = zeroconf.get_service_info(type, name)
            if info and ip in [socket.inet_ntoa(addr) for addr in info.addresses]:
                result.append(info.name)

        def update_service(self, zeroconf, type, name):
            pass

    zeroconf = Zeroconf()
    listener = Listener()
    ServiceBrowser(zeroconf, "_services._dns-sd._udp.local.", listener)
    time.sleep(2)
    zeroconf.close()

    if result:
        return result[0]
    return None

# --- Scan Result ---
def scan_network(pdst, progress_callback=None):
    arp_request_packet = scapy.ARP(pdst=pdst)
    combined_packet = broadcast_packet / arp_request_packet
    answered, _ = scapy.srp(combined_packet, timeout=2, verbose=0)

    data = []
    seen = set()

    total = len(answered)
    for idx, (_, receive) in enumerate(answered, start=1):
        ip = receive.psrc
        mac = receive.hwsrc

        if (ip, mac) in seen:
            continue
        seen.add((ip, mac))

        try:
            vendor = MacLookup().lookup(mac)
        except:
            vendor = "Unknown"

        hostname = get_hostname(ip)
        data.append([ip, mac, vendor, hostname])

        if progress_callback:
            progress_callback(idx, total)

    return data

# --- GUI ---
class NetworkScannerGUI:
    def __init__(self, master):
        self.root = master
        self.root.title("Baysal Network Scanner")
        self.root.geometry("1280x720")

        lbl = tk.Label(self.root, text="Baysal Network Scanner", font=("fixedsys", 30, "bold"))
        lbl.pack(padx=10, pady=10)

        columns = ["IP", "MAC Address", "Vendor", "Hostname"]
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        self.tree.pack(expand=True, fill="both", pady=10)

        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        btn_scan_net = tk.Button(frame, text="Scan Network", command=self.scan_network_btn,
                                 width=20, height=2, font=("fixedsys", 15))
        btn_scan_net.grid(row=0, column=0, padx=10, pady=10)

        btn_scan_host = tk.Button(frame, text="Scan Single Host", command=self.scan_host_btn,
                                  width=20, height=2, font=("fixedsys", 15))
        btn_scan_host.grid(row=0, column=1, padx=5)

        btn_exit = tk.Button(frame, text="Exit", command=self.root.quit,
                             width=20, height=2, font=("fixedsys", 15))
        btn_exit.grid(row=0, column=2, padx=5)

        # progress bar
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=640, mode="determinate")
        self.progress.pack(pady=10)

    def clear_table(self):
        self.tree.delete(*self.tree.get_children())

    def update_progress(self, current, total):
        self.progress["maximum"] = total
        self.progress["value"] = current
        self.root.update_idletasks()

    def scan_network_btn(self):
        self.clear_table()
        self.progress["value"] = 0
        results = scan_network("192.168.1.0/24", progress_callback=self.update_progress)
        self.progress["value"] = 0
        if not results:
            messagebox.showerror("Error", "No devices found")
        for ip, mac, vendor, hostname in results:
            self.tree.insert("", "end", values=(ip, mac, vendor, hostname))

    def scan_host_btn(self):
        target_ip = simpledialog.askstring("Target IP", "Enter Target IP:")
        if not target_ip:
            return
        self.clear_table()
        self.progress["value"] = 0
        results = scan_network(target_ip, progress_callback=self.update_progress)
        self.progress["value"] = 0
        if not results:
            messagebox.showerror("Error", "Host not found")
        for ip, mac, vendor, hostname in results:
            self.tree.insert("", "end", values=(ip, mac, vendor, hostname))


if __name__ == "__main__":
    auto_update_vendor()
    root = tk.Tk()

    icon_path = "logo.png"
    try:
        img = PhotoImage(file=icon_path)
        root.iconphoto(False, img)
    except Exception:
        pass

    app = NetworkScannerGUI(root)
    root.mainloop()
