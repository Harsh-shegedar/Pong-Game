from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.hideturtle()
        self.Suar = 0
        self.harsh = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.goto(-170, 220)
        self.write(self.Suar, align="center", font=("courier", 40, "normal"))
        self.goto(170, 220)
        self.write(self.harsh, align="center", font=("courier", 40, "normal"))

    def l_point(self):
        self.Suar += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.harsh += 1
        self.clear()
        self.update_scoreboard()