#!/usr/bin/python2.7 

import socket
import struct

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

#bound to interface
rawSocket.bind(("lo", socket.htons(0x0800)))

# simple packet that contains the destination, source and ehtertype (this is ethertype ip)
packet = struct.pack("!6s6s2s", '\xaa\xaa\xaa\xaa\xaa\xaa', '\xbb\xbb\xbb\xbb\xbb\xbb', '\x08\x00')

rawSocket.send(packet + "Hello there")
