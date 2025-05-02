from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Create paddles
left_paddle = Paddle()
left_paddle.goto(-350, 0)

right_paddle = Paddle()
right_paddle.goto(350, 0)

ball = Ball()

# Key bindings
screen.listen()
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")

game_is_on = True

while game_is_on:
    ball.move()

    # Check for ball collision with top and bottom walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Check for ball collision with paddles
    if (340 < ball.xcor() < 350) and (
            right_paddle.ycor() + 50 > ball.ycor() > right_paddle.ycor() - 50):
        ball.bounce_x()

    if (-340 > ball.xcor() > -350) and (
            left_paddle.ycor() + 50 > ball.ycor() > left_paddle.ycor() - 50):
        ball.bounce_x()

    # If ball goes out of bounds (left or right side), reset it
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.refresh()

    screen.update()

screen.exitonclick()
