from turtle import *
screensize(3000,3000)
m =25
tracer(False)

for i in range(8):
    fd(3*m)
    rt(90)
    fd(6*m)
    lt(90)

    fd(8 * m)
    rt(90)
    bk(5 * m)
    lt(90)

    bk(5 * m)
    rt(90)
    bk(5 * m)
    lt(90)

    bk(6 * m)
    rt(90)
    fd(2 * m)
    lt(90)
pu()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*m,y*m)
        dot(3,'red')
goto(0,0)
dot(10,'red')
update()
done()
