from scapy.all import ARP, Ether, srp
import socket
        
def scan_network(ip_range):
    # Membuat paket ARP request
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]
    devices = []

    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

devices = scan_network("192.168.1.0/24")  # Ganti dengan IP range kamu


def is_printer(ip):
    ports = [9100, 631, 515]  # JetDirect, IPP, LPD
    open_ports = []
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((ip, port)) == 0:
                open_ports.append(port)
    return open_ports

print("\n=== 🔍 Scanning Printer Ports ===")
for device in devices:
    ip = device['ip']
    open_ports = is_printer(ip)
    if open_ports:
        print(f"🎯 Possible printer found at {ip} | Open ports: {open_ports}")
        
def lookup_mac_vendor(mac):
    try:
        url = f"https://api.macvendors.com/{mac}"
        response = requests.get(url, timeout=5)
        return response.text
    except:
        return "Unknown Vendor"

for device in devices:
    vendor = lookup_mac_vendor(device['mac'])
    print(f"{device['ip']} - {device['mac']} ({vendor})")

print("Devices on network:")
for d in devices:
    print(d)
