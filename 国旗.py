#五星红旗
from turtle import *
setup(700,500,50,50)
penup()
fd(-300)
left(90)
fd(200)
#国旗轮廓
pendown()
color('red','red')
begin_fill()
for i in range(2):
    right(90)
    fd(600)
    right(90)
    fd(400)
end_fill()
#大五角星
right(90)
fd(100)
right(90)
fd(40)
left(18)
color('yellow','yellow')
begin_fill()
for i in range(5):
    fd(120)
    right(144)
end_fill()

#第一个小五角星
penup()
right(18)
fd(60)
left(120.96)
fd(96.62)
left(18)
pendown()
color('yellow','yellow')
begin_fill()
for i in range(5):
    fd(20)
    right(144)
end_fill()

#第二个小五角星
penup()
right(198)
fd(96.62)
right(180+30.96-8.13)
fd(141.4-20)
left(18)
pendown()
color('yellow','yellow')
begin_fill()
for i in range(5):
    fd(20)
    right(144)
end_fill()

#第三个小五角星
penup()
right(198)
fd(141.4-20)
right(180+8.13+15.95)
fd(145.6-20)
left(18)
pendown()
color('yellow','yellow')
begin_fill()
for i in range(5):
    fd(20)
    right(144)
end_fill()

#第四个小五角星
penup()
right(198)
fd(145.6-20)
right(180-15.95+38.66)
fd(128-20)
left(18)
pendown()
color('yellow','yellow')
begin_fill()
for i in range(5):
    fd(20)
    right(144)
end_fill()

hideturtle()
