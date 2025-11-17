import turtle
t = turtle.Turtle()
t.speed(10)
# t.color("---") changes color of pen
t.color("maroon")
for i in range(70):
    t.goto(-200, 200)
    t.forward(300 +i )
    t.left(90)
    t.forward(500 + i)

t.color("purple")
for i in range(70):
    t.forward(80 + i)
    t.left(80 + i)
    t.goto(100, 100)
t.goto(200, 75)
for i in range(80):
    t.right(50)
    t.forward(90)
t.left(90 + 2 * i)
t.forward(100)
# the green spikes
t.color("lime")
for i in range(40):
    t.forward (30 + i + 6)
    t.left (78 * i)
    t.forward (89 * i)
    t.goto(100, 100 + i)
t.color("white")
t.goto(-200, -200)
for i in range(40):
    t.left(123 + i)
    t.forward(100 + i)
    t.color("black")
turtle.exitonclick()

