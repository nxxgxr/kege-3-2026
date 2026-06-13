from ipaddress import *

ip = ip_address('153.202.16.37')
ans = []
for mask in range(33):
    net = ip_network(f'{ip}/{mask}', False)
    if net.network_address == ip_address('153.202.16.32'):
        print(net.netmask)
print(255+248)
