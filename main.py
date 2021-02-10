import turtle as t
import random

polygon = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

for i in range(3, 10):
    num_sides = i
    side_length = 70
    angle = 360.0 / num_sides
    polygon.color(random.choice(colours))
    for i in range(num_sides):

        polygon.forward(side_length)
        polygon.right(angle)


