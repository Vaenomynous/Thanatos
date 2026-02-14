import scapy.all as scapy
import socket

def arp_scan(ip_range):
    print("Starting ARP scan...")
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    live_hosts = []
    for element in answered_list:
        live_hosts.append(element[1].psrc)
    return live_hosts

def port_scan(ip, ports):
    open_ports = []
    print(f"Scanning ports on {ip}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    ip_range = "192.168.1.1/24"  # change to your local network
    discovered_hosts = arp_scan(ip_range)
    print(f"Discovered Hosts: {discovered_hosts}")
    
    ports_to_scan = range(1, 1024)
    for host in discovered_hosts:
        open_ports = port_scan(host, ports_to_scan)
        print(f"Open ports on {host}: {open_ports}")