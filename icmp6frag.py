# Envio de paquetes fragmentados ICMPv6 Echo Request con scapy
# (c) hackingyseguridad.com 2017
from scapy.all import *
sip = 'fe80::216:35ff:fe0c:dba5'
dip = '2a00:1450:4003:801::200e'
packets = fragment6(IPv6(src=sip, dst=dip) / IPv6ExtHdrFragment() / ICMPv6EchoRequest(data='A'*5000), 1024)
send(packets)
