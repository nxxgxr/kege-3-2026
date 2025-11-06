from turtle import *
tracer(False)
screensize(4000,4000)
m=13

for i in range(5):
    fd(37*m)
    rt(90)
    fd(44*m)
    rt(90)
pu


bk(18*m)
rt(90)
fd(29*m)
lt(90)

pd

for i in range(5):
    fd(31*m)
    rt(90)
    fd(35*m)
    rt(90)

up()
for x in range(0,60):
    for y in range(-60,40):
        goto(x*m,y*m)
        dot(3,'red')




update()
done()