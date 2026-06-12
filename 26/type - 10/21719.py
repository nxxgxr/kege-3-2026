with open(r'../files/26_21719.txt') as file:
    n=int(file.readline())
    students={}
    for line in file:
        ID,num = map(int,line.split())
        if ID not in students:
            students[ID] = {num}
        else:
            students[ID] |= {num}
ans=[]
for ID in students:
    tasks = sorted(students[ID])
    cnt=1
    for i in range(len(tasks)-1):
        if tasks[i+1] - tasks[i] == 2:
            cnt+=1
            ans+=[[cnt,ID]]
        else:
            cnt=1
print(max(ans,key=lambda x: (x[0],-x[1])))





