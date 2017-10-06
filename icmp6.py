# Envio de paquetes fragmentados ICMPv6 Echo Request con scapy
# (c) hackingyseguridad.com 2017
from scapy.all import *
sip = 'fe80::20c:29ff:fe67:22c2'
dip = 'fe80::700d:da7e:80bb:aca9'
packets = fragment6(IPv6(src=sip, dst=dip) / IPv6ExtHdrFragment() / ICMPv6EchoRequest(data='A'*5000), 1024)
send(packets)
