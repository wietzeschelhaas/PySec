#!/usr/bin/python2.7 
from scapy.all import *


for lsb in range(1,50):
	ip = "192.168.1." +str(lsb)
	arpReq = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip, hwdst ="ff:ff:ff:ff:ff:ff")
	# send the arpReq packet and receive 1 packet. verbose=0 means that its not in verbose mode
	arpRes = srp1(arpReq, timeout=1, verbose=0)
	# if we got a response
	if arpRes:
		print "IP: " + arpRes.psrc + " MAC: " + arpRes.hwsrc

