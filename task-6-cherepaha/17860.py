from turtle import *
tracer(False)
screensize(4500,4500)
m=35

for i in range(4):
    fd(22*m)
    rt(90)
    fd(6*m)
    rt(90)
pu


fd(1*m)
rt(90)
fd(5*m)
lt(90)

pd

for i in range(9):
    fd(53*m)
    rt(90)
    fd(75*m)
    rt(90)

up()
for x in range(0,100):
    for y in range(-120,10):
        goto(x*m,y*m)
        dot(3,'red')




update()
done()