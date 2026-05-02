with open(r'./26_17643.txt') as file:
    n=int(file.readline())
    data=[list(map(int,i.split())) for i in file]

# print(data)
kl=set([i[0] for i in data])
# print(kl)
# kl={12,11,15}
# data=[[12,3,1],[11,2,5],[15,5,1],[12,3,0]]
kolvo=[]
sredcen=sum([i[1] for i in data])/n
print(sredcen)
for i in kl:
    cnt=0
    for b in data:
        if b[1] > sredcen:
        # print(i,b[0],cnt)
            if i==b[0] and b[2]==0:
                cnt+=1
    if cnt>40:
        vsego=0
        for x in data:
            if x[0]==i:
                vsego+=1
        ostalos=vsego-cnt
        kolvo += [(cnt,ostalos,b[1],i)]

print(kolvo)



print(51*856,36)

