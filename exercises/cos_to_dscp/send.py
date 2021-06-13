#!/usr/bin/env python
import argparse
import sys
import socket
import random
import struct

from scapy.all import sendp, send, get_if_list, get_if_hwaddr
from scapy.all import Packet
from scapy.all import Ether, IP, UDP, TCP, Dot1Q

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

    if len(sys.argv) < 3:
        print 'pass 2 arguments: <destination> <802.1q priority>'
        exit(1)
    
    priority = int(sys.argv[2])

    if priority < 0 or priority > 7:
        print 'Priority must be between 0 and 7'
        exit(1)

    addr = socket.gethostbyname(sys.argv[1])
    iface = get_if()


    print "sending on interface %s to %s" % (iface, str(addr))
    pkt =  Ether(src=get_if_hwaddr(iface), dst='ff:ff:ff:ff:ff:ff')
    pkt = pkt /Dot1Q(prio=priority, vlan=1) /IP(dst=addr) / TCP(dport=1234, sport=random.randint(49152,65535)) / "Test"
    pkt.show2()
    sendp(pkt, iface=iface, verbose=False)


if __name__ == '__main__':
    main()
