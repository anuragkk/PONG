from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1)
        self.color("yellow")
        self.penup()
        self.speed("slow")
        self.x_move = 6
        self.y_move = 6

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def refresh(self):
        missed_side = None

        if self.xcor() > 390:  # Ball missed by the right paddle
            self.goto(0, 0)  # Reset to center
            self.x_move = -10  # Move left after right paddle miss

            missed_side = 'right'  # Ball missed by the right side

        elif self.xcor() < -390:  # Ball missed by the left paddle
            self.goto(0, 0)  # Reset to center
            self.x_move = 10  # Move right after left paddle miss

            missed_side = 'left'  # Ball missed by the left side

        return missed_side  # Return the side which missed the ball (right/left)






