from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("purple")
        self.speed("fastest")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=5)

    def go_up(self):
        x_position = self.xcor()
        y_position = self.ycor() + 20
        if y_position < 250:
            self.goto(x_position, y_position)

    def go_down(self):
        x_position = self.xcor()
        y_position = self.ycor() - 20
        if y_position > -250:  # Stop before bottom edge
            self.goto(x_position, y_position)
