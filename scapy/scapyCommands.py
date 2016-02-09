
#______________________________________#
#Injecting							   #
#______________________________________#

#google bpf for all filters
packets = sniff(iface="wlan0", filter="icmp", count=3)  #sniffs 3 icmp packets on wlan0, note that arguemnts are optional

#creates an ip packet
pkt = IP()
# show the ip packet
pkt.show()

# create a ICMP packet, as a default this will create a echo request packet (ping)
# the destination is google, you can manipulate any header field in the '()'
#"this is some data" is just some raw data in the packet
pkt = IP(dst="google.com")/ICMP()/"This is some data"

#sends the packet on layer 3
send(pkt)

#sending on layer 2, note that when using sendp you have to construct the ether header yourself and also specify the interface on which the packet has to be send
#XXX is the data attached
#this will loop forever, and send a packet in a interval of 1 seconds
sendp(Ether()/IP(dst="google.com")/ICMP()/"XXX", iface="eth1", loop=1, inter=1)


#sends packet and receives packets, this is going to wait for a response
# this is going to timeout after 5 seconds
sr(IP(dst="google.com")/ICMP()/"XXX" , timeout=5)
#stores the response in a variable, _ = last received packet
response = _
# to see the received packet
response[0]

# waits for a single answer
sr1(IP(dst="google.com")/ICMP()/"XXX")


#______________________________________#
#SNIFFING							   #
#______________________________________#

#this prints the packet driectly, prn is called everytime which calls summary
# this does also work with show
packets = sniff(iface="wlan0", filter="icmp", count=30, prn=lambda x: x.summary()) 

packets[n].show() # shows packet n 

hexdump(packets[n])  #show packet n in hex

wrpcap("demo.pcap", packets)  #writes packets to a pcap file

readPackets = rdpcap("demo.pcap") #reads pcap file

strPacket = str(packets[0]) # prints the packet as a string
export_object(strPacket) # export packet as base64 encoded
newPacket = import_object() # imports it again


