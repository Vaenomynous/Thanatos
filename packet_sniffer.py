import scapy.all as scapy

class PacketSniffer:
    def __init__(self):
        self.packets = []

    def start_sniffing(self):
        scapy.sniff(prn=self.process_packet, store=False)

    def process_packet(self, packet):
        self.packets.append(packet)
        print(packet.summary())  # Print packet summary for inspection

if __name__ == '__main__':
    sniffer = PacketSniffer()
    print('Starting packet capture...')
    sniffer.start_sniffing()