from turtle import  Turtle
class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("pink")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        self.score = 0
        self.update_score()
