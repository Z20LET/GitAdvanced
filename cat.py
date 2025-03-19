import turtle


def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.circle(radius)
    turtle.end_fill()


def draw_triangle(color, x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()


def draw_eyes(x, y, radius):
    draw_circle("white", x - radius, y, radius)
    draw_circle("white", x + radius, y, radius)
    draw_circle("black", x - radius, y, radius / 2)
    draw_circle("black", x + radius, y, radius / 2)


def draw_nose(x, y):
    draw_triangle("pink", x, y - 10, 20)


def draw_mouth(x, y):
    turtle.penup()
    turtle.goto(x, y - 20)
    turtle.setheading(-60)
    turtle.pendown()
    turtle.circle(20, 120)
    turtle.penup()
    turtle.goto(x, y - 20)
    turtle.setheading(-120)
    turtle.pendown()
    turtle.circle(20, -120)


def draw_whiskers(x, y):
    turtle.penup()
    turtle.goto(x - 70, y - 10)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(50)

    turtle.penup()
    turtle.goto(x - 70, y - 20)
    turtle.setheading(10)
    turtle.pendown()
    turtle.forward(50)

    turtle.penup()
    turtle.goto(x - 70, y - 30)
    turtle.setheading(-10)
    turtle.pendown()
    turtle.forward(50)

    turtle.penup()
    turtle.goto(x + 20, y - 10)
    turtle.setheading(180)
    turtle.pendown()
    turtle.forward(50)

    turtle.penup()
    turtle.goto(x + 20, y - 20)
    turtle.setheading(170)
    turtle.pendown()
    turtle.forward(50)

    turtle.penup()
    turtle.goto(x + 20, y - 30)
    turtle.setheading(190)
    turtle.pendown()
    turtle.forward(50)


def draw_cat_face():
    draw_circle("orange", 0, 0, 100)
    draw_triangle("orange", -100, 140, 80)
    draw_triangle("orange", 20, 140, 80)
    draw_triangle("pink", -90, 120, 60)
    draw_triangle("pink", 30, 120, 60)
    draw_eyes(0, 50, 20)
    draw_nose(0, 30)
    draw_mouth(0, 20)
    draw_whiskers(0, 30)


if __name__ == "__main__":
    turtle.speed(5)
    draw_cat_face()
    turtle.hideturtle()
    turtle.done()
