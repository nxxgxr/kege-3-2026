from turtle import *
screensize(3000,3000)
tracer(False)
m=25

for i in range(4):
    fd(10*m)
    rt(270)
pu()
fd(3*m)
rt(270)
fd(5*m)
rt(90)
pd()
for i in range(2):
    fd(10*m)
    rt(270)
    fd(12*m)
    rt(270)

pu()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*m,y*m)
        dot(3,'red')
update()
done()