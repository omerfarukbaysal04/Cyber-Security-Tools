===================================================
              MAC CHANGER v1.0 - Python Tool
===================================================

Author   : omerfarukbaysal04  
GitHub   : https://github.com/omerfarukbaysal04  
Platform : Linux (Kali, Ubuntu, etc.)  
Language : Python 
Version  : 1.0

---------------------------------------------------
🛠️ DESCRIPTION:
This tool allows you to change the MAC address of a specified network interface (e.g., eth0) easily.  
It works via the terminal using the `-i` (interface) and `-m` (mac address) arguments.

---------------------------------------------------
📦 REQUIREMENTS:
- Python 
- Root privileges (to change MAC address)
- `ifconfig` command must be installed (`net-tools` package)

---------------------------------------------------
🚀 USAGE:
Run the script in the terminal like this:

    sudo python mac_changer.py -i <interface_name> -m <new_mac_address>

Example:
    sudo python mac_changer.py -i eth0 -m 00:11:22:33:44:55

---------------------------------------------------
🔍 WHAT IT DOES:
1. Disables the specified network interface.
2. Assigns the new MAC address.
3. Reactivates the interface.
4. Verifies if the MAC address has been successfully changed.

---------------------------------------------------
❗ NOTES:
- The MAC address must be in a valid format (e.g., `00:11:22:33:44:55`).
- The interface name must match an actual device (check with `ifconfig`).
- This script works only on Linux systems (not for Windows).
- On some systems, `ip` is used instead of `ifconfig`. (Future versions may support `ip` command.)

---------------------------------------------------
© 2025 - omerfarukbaysal04
