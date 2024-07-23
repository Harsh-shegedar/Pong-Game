from turtle import Turtle, Screen
from stick import Stick
from ball import Ball
import time
from scoreboard import ScoreBoard



screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

lpaddle = Stick((-350, 0))
rpaddle = Stick((350, 0))
ball = Ball()
scoreboard = ScoreBoard()





screen.listen()
screen.onkey(lpaddle.moveleft, "a")
screen.onkeypress(lpaddle.moveleft, key="a")
screen.onkey(lpaddle.moveright, "s")
screen.onkeypress(lpaddle.moveright, key="s")
screen.onkey(rpaddle.moveleft, "Up")
screen.onkeypress(rpaddle.moveleft, key="Up")
screen.onkey(rpaddle.moveright, "Down")
screen.onkeypress(rpaddle.moveright, key="Down")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(rpaddle) < 49 or ball.xcor() < -320 and ball.distance(lpaddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



















screen.exitonclick()