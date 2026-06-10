with open(r'./files/24_4682.txt') as file:
    data=file.readline()


l=dlina=flag=ans=0
for r in range(len(data)):

    if data[r] in 'AE' and flag==0:
        flag=1
        l=r
    elif data[r] in 'BCD' and flag==1:
        flag=2
        dlina = r - l + 1
    elif data[r] in 'AE' and flag==2:
        flag=1
        dlina=r-l+1
    else:
        l=r
        flag=0
    ans=max(ans,dlina)
print(ans/2)

