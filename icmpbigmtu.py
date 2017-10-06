# Envio de paquetes ICMPv6 PacketTooBig MTU 1500 con scapy
# (c) hackingyseguridad.com 2017
from scapy.all import *
dip = '2a00:1450:4003:801::200e'
icmp = IPv6(dst=dip)/ICMPv6PacketTooBig(mtu=1280)
icmp.show()
send(icmp, iface="lo")
