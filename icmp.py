# Envio de paquetes ICMPv6 Echo Request con scapy
# (c) hackingyseguridad.com 2017
from scapy.all import *
sip = 'fe80::216:35ff:fe0c:dba5'
dip = '2a00:1450:4003:801::200e'
sr1(IPv6(dst=dip)/ICMPv6EchoRequest())
