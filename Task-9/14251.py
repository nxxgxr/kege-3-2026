
with open(r'./files/14251.txt') as file:
    data=[list(map(int,i.split())) for i in file]

for line in data:
    amount=[line.count(i) for i in set(line)]
    pov=[i for i in line if line.count(i)>1]
    ne_pov=[i for i in line if line.count(i)==1]
    ne_chet = [i for i in line if i%2==1]
    if sorted(amount)==[1,1,1,2,2]:
        if sum(pov)<=sum(ne_chet):
            print(sum(line))
            break
