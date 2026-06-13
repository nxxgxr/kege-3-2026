from turtle import *
screensize(3000,3000)
m=30
tracer(False)

fd(30*m)
fd(24*m)
lt(60)
rt(240)

fd(54*m)
lt(120)
fd(24*m)
lt(60)

pu()
fd(30*m)
rt(90)
fd(20*m)
lt(90)

pd()

for i in range(17):
    fd(6*m)
    lt(90)
    fd(80*m)
    lt(90)
pu()

for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(3,'red')
update()
done()