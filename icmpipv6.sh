#!/bin/bash
echo
echo "...Script para envio de ping Icmp IPv6" 
echo "Uso: ./icmpipv6.sh IPv6 Num_peticiones"
echo "Por ejemplo google.com 2a00:1450:4003:801::200e"
for i in 1 `seq 1 $2`
do
ping6 $1
done
