from turtle import *
tracer(False)
screensize(4000,4000)
m=70

lt(90)

up()
for i in range(10):
    rt(120)
    fd(10*m)
down()
for i in range(7):
    fd(15*m)
    rt(90)
for i in range(5):
    rt(60)
    fd(20*m)
    rt(30)




up()
for x in range(0,30):
    for y in range(-40,00):
        goto(x*m,y*m)
        dot(3,"red")

update()
done()