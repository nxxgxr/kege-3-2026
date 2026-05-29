from turtle import *
screensize(3000,3000)
m=25
tracer(False)

for i in range(2):
    fd(20*m)
    rt(90)
    fd(12*m)
    rt(90)

pu()
fd(9*m)
rt(90)
fd(7*m)
lt(90)

pd()
for i in range(2):
    fd(13*m)
    rt(90)
    fd(6*m)
    rt(90)

pu()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*m,y*m)
        dot(3,'red')

update()
done()