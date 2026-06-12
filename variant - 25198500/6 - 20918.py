from turtle import *
screensize(3000,3000)
m=20
tracer(False)

for i in range(3):
    fd(27*m)
    rt(90)
    fd(12*m)
    rt(90)

pu()
fd(4*m)
rt(90)
fd(6*m)
lt(90)
pd()
for i in range(4):
    fd(83*m)
    rt(90)
    fd(77*m)
    rt(90)
pu()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*m,y*m)
        dot(3,'red')
update()
done()