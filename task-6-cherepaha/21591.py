from turtle import *
tracer(False)

screensize(4000,4000)
m=40

rt(270)
for i in range(2):
    fd(8*m)
    rt(120)

rt(120)
for i in range(2):
    rt(120)
    fd(3*m)
    rt(240)

rt(240)



for i in range(2):
    fd(14*m)
    rt(120)


up()
for x in range(0,20):
    for y in range(-20,15):
        goto(x*m,y*m)
        dot(3,'red')




update()
done()