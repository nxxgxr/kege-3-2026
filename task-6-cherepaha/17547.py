from turtle import *
tracer(False)
screensize(3000,3000)
m=15

for i in range(3):
    fd(7*m)
    rt(90)
    fd(12*m)
    rt(90)
pu


fd(4*m)
rt(90)
fd(6*m)
lt(90)

pd

for i in range(4):
    fd(83*m)
    rt(90)
    fd(77*m)
    rt(90)

up()
for x in range(-80,10):
    for y in range(-15,80):
        goto(x*m,y*m)
        dot(3,'red')




update()
done()