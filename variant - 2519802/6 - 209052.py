from turtle import *
screensize(3000,3000)
m=45
tracer(False)

for i in range(5):
    fd(6*m)
    rt(90)
    fd(3*m)
    rt(90)
pu()
fd(4*m)
rt(90)
fd(2*m)
rt(90)
pd()
for i in range(8):
    fd(8*m)
    rt(90)
    fd(5*m)
    rt(90)
pu()
fd(4*m)
rt(90)
fd(2*m)
lt(90)
pd()
for i in range(4):
    fd(5*m)
    lt(90)
pu()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(3,'red')

update()
done()