#!/usr/bin/python2.7 

import socket
import struct
import binascii

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

rawSocket.bind(("lo", socket.htons(0x0800)))
# the '!' is to tell struct to use big endian
ethHeader = struct.pack("!6s6s2s", '\xaa\xaa\xaa\xaa\xaa\xaa', '\xbb\xbb\xbb\xbb\xbb\xbb', '\x08\x06')
arpHeader = struct.pack("!2s2s1s1s2s", '\x00\x01','\x08\x00', '\x06', '\x04', '\x00\x02')
arpSenderMac = struct.pack("!6s", '\xaa\xaa\xaa\xaa\xaa\xaa')
arpSenderIP = socket.inet_aton('192.168.2.111')
arpTargetMac = struct.pack("!6s", '\xbb\xbb\xbb\xbb\xbb\xbb')
arpTargetIP = socket.inet_aton('192.168.2.1')


packet = ethHeader + arpHeader + arpSenderMac + arpSenderIP + arpTargetMac + arpTargetIP

rawSocket.send(packet)