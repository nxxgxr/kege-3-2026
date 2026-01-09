from turtle import *
tracer(False)
screensize(22000,22000)
m=30

for i in range(2):
    fd(14*m)
    lt(270)
    bk(12*m)
    rt(90)

up()
fd(9*m)
rt(90)
bk(12*m)
lt(90)
pd()
for i in range(2):
    fd(13*m)
    rt(90)
    fd(6*m)
    rt(90)


up()
for x in range(-20,25):
    for y in range(-20,20):
        goto(x*m,y*m)
        dot(3,"red")

update()
done()