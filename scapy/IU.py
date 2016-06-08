from __future__ import division
from scapy.all import *
import socket
import struct
import binascii




hosts = {}
totalData = 1

def printHostProcentage():
	for key in hosts:
		print key + " uses " + str(int(float((hosts[key] / totalData)) * 100)) + "%"



print "Searchin for hosts, this may take a while"
for lsb in range(1,13):
	ip = "192.168.1." +str(lsb)
	arpReq = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip, hwdst ="ff:ff:ff:ff:ff:ff")
	arpRes = srp1(arpReq, timeout=1, verbose=0)
	if arpRes:
		hosts[arpRes.psrc] = 0

print ""
print "Done"
hosts["192.168.1.10"] = 0

printHostProcentage()

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800)) 
rawSocket.bind(("wlp3s0", 0)) 

while 1:
	packet = rawSocket.recvfrom(2048)


	# the ip header is 20 bytes long
	ipHeader = packet[0][14:34]
	# we are not interested in the first 16 bytes.
	ip_hdr = struct.unpack("!12s4s4s", ipHeader)
	for x in hosts:
		if socket.inet_ntoa(ip_hdr[2]) == x:
			hosts[x] = hosts[x] + len(packet[0])
			totalData += len(packet[0])
			print(chr(27) + "[2J")
			printHostProcentage()
		