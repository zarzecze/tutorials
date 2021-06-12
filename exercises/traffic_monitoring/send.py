#!/usr/bin/env python
import sys
import socket
import random
import time

from scapy.all import sendp, send, get_if_list, get_if_hwaddr
from scapy.all import Packet
from scapy.all import Ether, IP, UDP, TCP

def get_if():
    ifs=get_if_list()
    iface=None # "h1-eth0"
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print "Cannot find eth0 interface"
        exit(1)
    return iface

def main():

    if len(sys.argv) < 2:
        print 'usage: generate_load.py <destination>'
        exit(1)

    addr = socket.gethostbyname(sys.argv[1])
    iface = get_if()

    print "sending on interface %s to %s" % (iface, str(addr))
    try:
        while(True):
            msg = "A" * random.randint(500, 1000)
            pkt =  Ether(src=get_if_hwaddr(iface), dst='ff:ff:ff:ff:ff:ff')
            pkt = pkt /IP(dst=addr) / TCP(dport=1234, sport=random.randint(49152,65535)) / msg
            sendp(pkt, iface=iface, verbose=False)
            print "SENT"
            time.sleep(5)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()