from turtle import *
screensize(3000,3000)
m=25
tracer(False)

for i in range(3):
    fd(5*m)
    rt(90)
    bk(8*m)
    rt(90)

pu()
fd(2*m)
rt(90)
bk(3*m)
lt(90)
pd()

for i in range(3):
    fd(4*m)
    rt(90)
    bk(6*m)
    rt(90)

pu()
fd(4*m)
rt(180)
bk(2*m)
pd()
for i in range(2):
    fd(5*m)
    rt(90)
    bk(7*m)
    rt(90)

pu()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*m,y*m)
        dot(3,'red')

update()
done()