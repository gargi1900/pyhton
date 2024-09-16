# import colorgram
#
# colors = colorgram.extract('image.jpeg', 85)
# print(colors)
#
# rgb_colors = []
# for color in colors:
#     rgb_colors.append(color.rgb)
#
# print(rgb_colors)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(248, 228, 23), (212, 13, 10), (196, 14, 36), (35, 90, 186), (232, 149, 45), (193, 70, 23), (230, 228, 6),
              (44, 211, 73), (34, 31, 151), (17, 23, 55), (66, 10, 50), (241, 42, 148), (71, 200, 226),
              (15, 206, 223), (64, 21, 11), (220, 22, 110), (17, 154, 20), (229, 166, 11), (242, 65, 21), (248, 11, 9),
              (98, 75, 10), (221, 139, 195), (77, 239, 160), (11, 97, 63), (6, 37, 33), (78, 214, 149), (239, 158, 205),
              (99, 223, 231), (91, 85, 201), (249, 9, 12), (243, 165, 158), (177, 180, 225), (37, 243, 158),
              (11, 77, 113)]


tim.setheading(225)
tim.forward(310)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim. dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
