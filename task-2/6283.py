from itertools import *
ans=set()
def f(x,y,z,w):
    return (not((not(x<=(not w))) and z)) and (not(w<=z)) and (x<=(not z))

for i in product((0,1),repeat=5):
    table=[
        (1,0,i[0],0),
        (1,0,i[1],i[2]),
        (i[3],1,i[4],1)
    ]
    if len(table)==len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,t))) for t in table]==[1,0,0]:
                ans|={p}
print(len(ans))