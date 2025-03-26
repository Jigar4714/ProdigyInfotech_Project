from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = "TCP" if TCP in packet else "UDP" if UDP in packet else "Other"
        payload = packet[TCP].payload if TCP in packet else packet[UDP].payload if UDP in packet else "N/A"

        log_entry = f"Source IP: {src_ip} -> Destination IP: {dst_ip} | Protocol: {protocol} | Payload: {payload}"
        print(log_entry)

        with open("packet_logs.txt", "a") as log_file:
            log_file.write(log_entry + "\n")

print("Starting packet sniffer... Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=False)