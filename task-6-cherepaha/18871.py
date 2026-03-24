from turtle import *
screensize(3000,3000)
tracer(False)
m=25

for i in range(2):
    fd(10*m)
    rt(90)
    fd(20*m)
    rt(90)
pu()
bk(4*m)
rt(90)
fd(7*m)
lt(90)
pd()
for i in range(4):
    fd(8*m)
    lt(90)
    fd(12*m)
    lt(90)
pu()
fd(10*m)
pd()
for i in range(4):
    fd(12*m)
    rt(90)
pu()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*m,y*m)
        dot(3,'red')

update()
done()