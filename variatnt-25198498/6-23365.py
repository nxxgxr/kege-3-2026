from turtle import *
screensize(3000,3000)
m=15
tracer(False)

for i in range(3):
    fd(39*m)
    rt(90)
    fd(48*m)
    rt(90)
pu()
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
pu()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(3,'red')
update()
done()