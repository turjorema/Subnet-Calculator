import ipaddress
import time
import sys

# Colors
CYAN = "\033[96m"
PINK = "\033[95m"
GREEN = "\033[92m"
AMBER = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

print(CYAN + "=========================================")
print("        🧮  SUBNET CALCULATOR")
print("               v1.0")
print(PINK + "         Developed by 4RCH-M3G" + CYAN)
print("=========================================" + RESET)

ip_input = input("\nEnter IP address with CIDR (e.g. 192.168.1.10/24): ")

try:
    network = ipaddress.ip_network(ip_input, strict=False)
except ValueError:
    print(RED + "\nInvalid IP/CIDR format. Example: 192.168.1.10/24" + RESET)
    sys.exit()

# Calculating animation
sys.stdout.write("\nCalculating subnet")
for i in range(6):
    sys.stdout.write(".")
    sys.stdout.flush()
    time.sleep(0.15)   # total ~2.1 seconds
print()

hosts = list(network.hosts())
first_host = hosts[0] if hosts else "N/A"
last_host = hosts[-1] if hosts else "N/A"
usable_hosts = network.num_addresses - 2 if network.num_addresses > 2 else 0

print(CYAN + "\n-----------------------------------------" + RESET)
print(f"  Network Address   : {GREEN}{network.network_address}{RESET}")
print(f"  Broadcast Address : {GREEN}{network.broadcast_address}{RESET}")
print(f"  Subnet Mask       : {GREEN}{network.netmask}{RESET}")
print(f"  Wildcard Mask     : {GREEN}{network.hostmask}{RESET}")
print(f"  CIDR Notation     : {GREEN}/{network.prefixlen}{RESET}")
print(f"  Total Addresses   : {AMBER}{network.num_addresses}{RESET}")
print(f"  Usable Hosts      : {AMBER}{usable_hosts}{RESET}")
print(f"  First Usable Host : {GREEN}{first_host}{RESET}")
print(f"  Last Usable Host  : {GREEN}{last_host}{RESET}")
print(CYAN + "-----------------------------------------" + RESET)