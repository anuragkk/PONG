import time
from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=800)
screen.title("PONG_GAME")
screen.tracer(0)

# Paddles
l_paddle = Paddle()
l_paddle.goto(-270, 0)

r_paddle = Paddle()
r_paddle.goto(270, 0)

# Ball and Scores
ball = Ball()
l_score = Score((-100, 350))
r_score = Score((100, 350))

# Controls
screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# Game Loop
game_is_on = True
while game_is_on:
    time.sleep(0.07)  # Control speed
    screen.update()
    ball.move()

    # Wall collision
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    # Paddle collision (right paddle first)
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 250) or (ball.distance(l_paddle) < 50 and ball.xcor() < -250):
        ball.bounce_x()

    # Missed ball (left or right)
    missed = ball.refresh()
    if missed == "right":
        l_score.increase_score()
    elif missed == "left":
        r_score.increase_score()

screen.exitonclick()
