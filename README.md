# icmpipv6 

#!/bin/bash
# https://es.wikipedia.org/wiki/Neighbor_Discovery
# https://es.wikipedia.org/wiki/ICMPv6
# ndisc6 opcion IPv6 eth0
# https://linux.die.net/man/8/ndisc6
# rltraceroute6 IPv6
# ICMPv6 neighbor discovery requires two types of ICMPv6
# ICMPv6 Neighbor solicitation (ICMPv6 Type 135) 
# ICMPv6 neighbor advertisement (ICMPv6 type 136).
echo
echo "...Script para envio de n Icmp IPv6 Neigbord Discovery" 
echo "Uso: ./ipv6.sh IPv6 Num_peticiones"
for i in 1 `seq 1 $1`
do
echo $i
ndisc6 -1 $2 eth0
done
