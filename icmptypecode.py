# Envio de paquetes ICMPv6 type y code con scapy
# (c) hackingyseguridad.com 2017
from scapy.all import *
sip = 'fe80::216:35ff:fe0c:dba5'
dip = '2a00:1450:4003:801::200e'
a=IPv6(nh=58, dst=dip, version=6L, hlim=255, plen=64, fl=0L, tc=224L)
b=ICMPv6ND_RA(code=0, chlim=64, H=0L, M=0L, O=0L, routerlifetime=1800, P=0L, retranstimer=0, prf=0L, res=0L, reachabletime=0, type=134)
c=ICMPv6NDOptMTU(res=0, type=5, len=1, mtu=1500)
send(a/b/c)
