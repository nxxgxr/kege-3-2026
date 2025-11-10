from turtle import *
tracer(False)

screensize(4000,4000)
m=70

rt(90)
for i in range(7):
    rt(45)
    fd(11*m)
    rt(45)


up()
for x in range(-25,20):
    for y in range(-20,15):
        goto(x*m,y*m)
        dot(3,'red')




update()
done()