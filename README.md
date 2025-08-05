

# 🛡️ Cybersecurity Tools Collection

This repository includes a collection of Python-based cybersecurity tools developed for educational and ethical hacking purposes.

> ⚠️ These tools are intended strictly for learning and legal penetration testing with permission. The author is not responsible for any misuse.

---

## 📌 Tools Overview

---

### 1. 🔧 MAC Changer

**Description:**  
Changes the MAC address of a given network interface.

**Usage:**  
```bash
python mac_changer.py -i <interface> -m <new_mac>
````

**Example:**

```bash
python mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

---

### 2. 🕵️‍♂️ Basic Keylogger

**Description:**
Logs every keypress and sends logs to an email address at fixed intervals.

**Usage:**

* Configure your email and password in the `send_email()` function.
* Run the script:

```bash
python keylogger.py
```

**Note:**
Gmail may block less secure app access by default. You may need to enable "Allow less secure apps" or use an app password.

---

### 3. ⚔️ MITM (Man-in-the-Middle) ARP Spoofing Tool

**Description:**
Performs ARP poisoning between a target machine and the network gateway.

**Usage:**

```bash
python mitm.py -t <target_ip> -g <gateway_ip>
```

**Example:**

```bash
python mitm.py -t 192.168.1.5 -g 192.168.1.1
```

**Note:**
Use `CTRL + C` to stop and restore ARP tables.

---

### 4. 🌐 Bay Net Discover

**Description:**
Scans the local network to discover connected devices using ARP requests.

**Usage:**
Run the script and choose one of the following options:

* 1: Scan all devices in the local network.
* 2: Scan a specific IP address.
* 3: Exit

```bash
python net_discover.py
```

---

### 5. 📡 Packet Listener (Sniffer)

**Description:**
Sniffs packets from the given interface and extracts HTTP data.

**Usage:**

```bash
python packet_listener.py
```

**Note:**
Make sure you run this on a valid network interface (e.g., `eth0`) and with root privileges.

---

### 6. 🔐 Ransomware (Encrypt & Decrypt Files)

**Description:**
Encrypts all files in the current directory using a generated key, simulating ransomware behavior. A separate decryption script is used to recover the files.

**Usage - Encryption:**

```bash
python ransom.py
```

**Usage - Decryption:**

```bash
python ransomdecrypter.py
```

**Important:**
The encryption key is stored in `generatedkey.key`. Without this key, files cannot be decrypted.

---

## ⚙️ Requirements

Install necessary dependencies:

```bash
pip install cryptography scapy pynput
```

Some tools may require:

* **Root/Admin privileges**
* **Linux environment** (tested on Kali Linux)
* **Python 3.6+**

---

## 🧠 Disclaimer

This project is created for **educational purposes only**.
Do not use these tools on networks, systems, or devices without **explicit written permission**.

---

## 👤 Author

**Ömer Faruk Baysal**
📧 [omerfarukbaysal04@gmail.com](mailto:omerfarukbaysal04@gmail.com)
🌐 [GitHub](https://github.com/omerfarukbaysal04)
🌐 [LinkedIn](https://linkedin.com/in/baysal)

---



