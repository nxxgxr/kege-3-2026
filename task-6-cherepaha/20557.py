from turtle import *
screensize(2000,2000)
m=25
tracer(False)
print(25**2)
for i in range(4):
    fd(36*m)
    rt(90)
    fd(41*m)
    rt(90)

pu()
rt(90)
fd(20)
lt(90)
fd(20)
pd()
for i in range(4):
    fd(25*m)
    rt(90)

pu()
fd(7*m)
lt(90)
fd(7*m)
rt(90)
pd()
for i in range(7):
    fd(16*m)
    rt(90)
pu()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(3,'red')
update()
done()