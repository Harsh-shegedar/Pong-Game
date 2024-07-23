from turtle import Turtle, Screen

position = [(-350, 0), (350, 0)]


class Stick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(4.4, 1)
        self.up()
        self.goto(position)

    def moveleft(self):
        newy = self.ycor() + 40
        self.goto(self.xcor(), newy)

    def moveright(self):
        newy = self.ycor() - 40
        self.goto(self.xcor(), newy)


