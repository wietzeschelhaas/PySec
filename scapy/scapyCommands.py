#google bpf for all filters
packets = sniff(iface="wlan0", filter="icmp", count=3)  #sniffs 3 icmp packets on wlan0, note that arguemnts are optional

#this prints the packet driectly, prn is called everytime which calls summary
# this does also work with show
packets = sniff(iface="wlan0", filter="icmp", count=30, prn=lambda x: x.summary()) 

packets[n].show() # shows packet n 

hexdump(packets[n])  #show packet n in hex

wrpcap("demo.pcap", packets)  #writes packets to a pcap file

readPackets = rdpcap("demo.pcap") #reads packets

strPacket = str(packets[0]) # prints the packet as a string
export_object(strPacket) # export packet as base64 encoded
newPacket = import_object() # imports it again
