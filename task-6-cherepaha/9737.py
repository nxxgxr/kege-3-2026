from turtle import *
tracer(False)
screensize(2000,2000)
m = 30

for x in range(2):
    fd(10 *m)
    rt(90)
    fd(18 *m)
    rt(90)

for x in range(1):
    up()
    fd(5 *m)
    rt(90)
    fd(7 *m)
    lt(90)
for x in range(2):
    down()
    fd(10 *m)
    rt(90)
    fd(7 *m)
    rt(90)

up()
for x in range(-10,20):
    for y in range(-20,10):
        goto(x*m,y*m)
        dot(3,'red')




update()
done()