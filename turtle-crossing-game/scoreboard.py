from turtle import Turtle, Screen
screen = Screen()
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER!", align="center", font=FONT)
