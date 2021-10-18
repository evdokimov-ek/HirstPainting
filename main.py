# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpeg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tuple = (r, g, b)
#     rgb_colors.append(tuple)
#
# print(rgb_colors)
import random
import turtle as t

timmy = t.Turtle()

color_list = [(238, 224, 81), (205, 4, 74), (199, 164, 8), (238, 48, 132), (206, 75, 12), (109, 180, 219),
              (218, 161, 104), (235, 224, 4), (28, 190, 109), (11, 24, 64), (20, 107, 176), (15, 28, 178),
              (218, 133, 179), (7, 186, 216), (228, 167, 200), (211, 24, 151), (120, 191, 159), (7, 50, 26),
              (60, 21, 7), (125, 219, 234), (32, 136, 71), (192, 13, 4), (108, 88, 215), (141, 217, 202),
              (238, 63, 35), (69, 10, 27)]

t.colormode(255)
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = t.Screen()
screen.exitonclick()
