from turtle import *
tracer(False)
screensize(3000,3000)
m=25

for i in range(3):
    fd(39*m)
    rt(90)
    fd(48*m)
    rt(90)
up()
fd(27*m)
rt(90)
fd(24*m)
lt(90)
pd()
for i in range(3):
    fd(29*m)
    rt(90)
    bk(18*m)
    rt(90)

up()
for x in range(-40,40):
    for y in range(-60,20):
        goto(x*m,y*m)
        dot(3,'red')
update()
done()
