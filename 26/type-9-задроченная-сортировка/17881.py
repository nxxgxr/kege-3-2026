with open(r'../files/26_17881.txt') as file:
    n=int(file.readline())
    students_0=[]
    students_3=[]
    for i in file:
        id,*exs = map(int,i.split())
        if 2 not in exs:
            students_0 +=[[sum(exs) / 4,id]]
        if exs.count(2)==3:
            students_3+=[[sum(exs)/4,id]]

students_0=sorted(students_0,key=lambda x:(-x[0],x[1]))
students_3=sorted(students_3,key=lambda x:(-x[0],x[1]))

print(students_0[:n//4][-1][1],students_3[0][1])
