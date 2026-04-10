from ipaddress import *
ip1=ip_address('218.48.192.56')
ip2=ip_address('218.48.192.0')
cnt=0
for mask in range(16,25):
    net=ip_network(f'{ip1}/{mask}',False)
    if net.num_addresses - 2>=500:
        if ip1 in net.hosts():
            if net.network_address==ip2:
                cnt+=1
print(cnt)