#!/usr/bin/python2.7 

# This has to be run as root!
import socket
import struct
import binascii

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800)) # PF_packet tells the kernel to use the packet interface,
#filter specific interfaces
#rawSocket.bind(("lo", 3)) 

#Sock_raw is to indicate that the socket is a raw socket, 
#the last argument tells the socket that we are interested in the internet protocol,
# these values can be found in the /usr/include/linux/if_ether.h file, other interesting protocols can be found there, such as arp and 802.11

# this return a tuple, the first value in the tuple is the actual packet, hence the [0] down below
while 1:
	packet = rawSocket.recvfrom(2048)
	print packet
	# the ethernet header is always 14 bytes
	ethernetHeader = packet[0][0:14]
	# The first 6 bytes is the destination mac, the 6 bytes coming after is the source mac and the last 2 bytes is the ethertype, IP in our case

	#this returns a tuple with 3 elements 
	eth_hdr = struct.unpack("!6s6s2s", ethernetHeader)
	# the hexlify method returns the hexadecimal representation of the binary data
	destMac   = binascii.hexlify(eth_hdr[0])
	SourceMac = binascii.hexlify(eth_hdr[1])
	ethType   = binascii.hexlify(eth_hdr[2])

	# the ip header is 20 bytes long
	ipHeader = packet[0][14:34]
	# we are not interested in the first 12 bytes, the fours after are the source and destination ip's
	ip_hdr = struct.unpack("!12s4s4s", ipHeader)

	# initial part of the tcp ipHeader
	tcpHeader = packet[0][34:54]
	#unpack the tcp header and find the tcp port numbers:
	tcp_hdr = struct.unpack("!HH16s", tcpHeader)
	
	# the inet_ntoa function translates the ip to ascii (network to ascii)
	if socket.inet_ntoa(ip_hdr[1]) == '127.0.0.1' :

		print 50*"#"
		print " "
		print "Source IP: " + socket.inet_ntoa(ip_hdr[1])
		print "Destination IP: " + socket.inet_ntoa(ip_hdr[2])

		print "Destination MAC: " + destMac
		print "Source MAC: " + SourceMac
		print "ethType: " + ethType

		print "Source Port : ", tcp_hdr[0]
		print "Destination Port : ", tcp_hdr[1]

