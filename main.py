# this code was used to extract the top 30 most common colors in the painting and save it to a list.
# The list was then manually checked for backround colors, which were deleted.

# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
#
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     color_tuple = (red, green, blue)
#     rgb_colors.append(color_tuple)

import turtle as t
import random

t.colormode(255)

turtle = t.Turtle()
turtle.speed("fastest")
turtle.hideturtle()
turtle.penup()

color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176),
              (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49),
              (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86),
              (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162),
              (156, 212, 190), (87, 46, 33), (37, 45, 83)]


def draw_circle():
    turtle.color(random.choice(color_list))
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()


def draw_picture(x, y):
    for i in range(10):  # creates 10 rows of circles
        turtle.setposition(x, y)  # sets the turtle at a new y position at the beginning of each row
        for i in range(10):  # creates 10 circles
            draw_circle()
            turtle.forward(60)
        y += 60

draw_picture(-275, -275)

screen = t.Screen()
screen.exitonclick()
