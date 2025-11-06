from turtle import *
tracer(False)
screensize(4000,4000)
m=25

for i in range(4):
    fd(30*m)
    rt(90)
    fd(48*m)
    rt(90)
pu


fd(27*m)
rt(90)
fd(24*m)
lt(90)

pd

for i in range(4):
    fd(29*m)
    rt(90)
    bk(18*m)
    rt(90)

up()
for x in range(-30,40):
    for y in range(-50,10):
        goto(x*m,y*m)
        dot(3,'red')




update()
done()