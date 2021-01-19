from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.score = 0
        with open('highscore_data.txt', mode='r') as highscore:
            self.high_score = int(highscore.read())
            # print(self.high_score)
        self.setx(100), self.sety(270)
        self.write(f"Score: {self.score}", False, align="center", font=("Comicsans", 15, "normal"))
        self.goto(-100, 270)
        self.write(f"High Score: {self.high_score}", False, align="center", font=("Comicsans", 15, "normal"))

    def update_score(self):
        self.clear()
        self.goto(100, 270)
        self.write(f"Score: {self.score}", False, align="center", font=("Comicsans", 15, "normal"))
        self.goto(-100, 270)
        self.write(f"High Score: {self.high_score}", False, align="center", font=("Comicsans", 15, "normal"))

    def change_score(self):
        self.score += 1
        self.update_score()

    def sethigh_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('highscore_data.txt', mode='w') as highscore:
                highscore.write(str(self.high_score))

        self.score = 0
        self.update_score()
