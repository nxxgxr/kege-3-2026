from ipaddress import *
net=ip_network('172.95.116.174/255.255.192.0',False)

set=net.hosts()
print(*set)
print(172+95+64+1)


