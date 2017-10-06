#!/bin/bash
echo
echo "...Script para envio de ping Icmp IPv6" 
echo "Por ejemplo IPv6 google.com 2a00:1450:4003:801::200e"
ping6 -c2 -I eth0 2a00:1450:4003:801::200e && echo -e "\nIPv6 Neighbours:\n" && ip -6 neigh
