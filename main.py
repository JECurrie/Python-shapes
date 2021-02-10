import turtle

polygon = turtle.Turtle()

for i in range(3, 10):
    num_sides = i
    side_length = 70
    angle = 360.0 / num_sides

    for i in range(num_sides):
        polygon.forward(side_length)
        polygon.right(angle)


turtle.done()