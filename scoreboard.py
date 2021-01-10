from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.score = 0
        self.setx(0), self.sety(270)
        self.write(f"Score: {self.score}", False, align="center", font=("Comicsans", 15, "normal"))

    def change_score(self):
        self.score += 1
        self.write(f"Score: {self.score}", False, align="center", font=("Comicsans", 15, "normal"))