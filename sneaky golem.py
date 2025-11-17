import turtle
t = turtle.Turtle()
t.speed(10)

t.color("black")
for i in range(50):
    t.goto(0, 0)
    t.forward(80 + i )
    t.left(130)
    t.forward(70 + i + 3)
t.color("violet")
for i in range(20):
    t.goto(0, 0)
    t.forward(70 * i )
    t.left(130)
    t.forward(40 + i)
t.color("crimson")
t.goto(50, 50)
for i in range(40):
    t.goto(0, 0)
    t.left(123 + i)
    t.forward(400 + i)
turtle.exitonclick()