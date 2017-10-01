# icmpipv6 

#!/bin/bash
# https://es.wikipedia.org/wiki/Neighbor_Discovery
# https://es.wikipedia.org/wiki/ICMPv6
# ndisc6 opcion IPv6 eth0
# https://linux.die.net/man/8/ndisc6
https://github.com/ArthurChiao/ndisc6-standalone
# rltraceroute6 IPv6
# ICMPv6 neighbor discovery requires two types of ICMPv6
# ICMPv6 Neighbor solicitation (ICMPv6 Type 135) 
# ICMPv6 neighbor advertisement (ICMPv6 type 136).
# https://www.youtube.com/watch?v=_rXH8XpXXQ0
# rltraceroute6 IPv6.
# tcptraceroute6, a TCP/IPv6-based traceroute implementation,
# tracert6, a ICMPv6 Echo Request based traceroute,
# tcpspray6, a TCP/IP Discard/Echo bandwidth metter.
# Sending Multicast Ping Requets
# ping6 -c5 ff02::1 -I eth0
# IPv6 Addresses
# ip -6 neigth
# Scan con Nessus
neighbour discovery:

# trigger the discovery
ping6 -c2 -I eth0 ff02::1
# print the results:
ip -6 neigh
Or with the network interface specified in a shell variable and the commands put in a single command line:

IFACE=eth0
ping6 -c2 -I $IFACE ff02::1 && echo -e "\nIPv6 Neighbours:\n" && ip -6 neigh



echo
echo "...Script para envio de n Icmp IPv6 Neigbord Discovery" 
echo "Uso: ./ipv6.sh IPv6 Num_peticiones"
for i in 1 `seq 1 $1`
do
echo $i
ndisc6 -1 $2 eth0
done
