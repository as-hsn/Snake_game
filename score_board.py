from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Georgia', 18, 'normal')



class ScoreBoard (Turtle):
    def __init__(self) :
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup ()
        self.goto(-20 ,265)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write (f"Score = {self.score}          High Score = {self.high_score}",
                    move=False,
                    align=ALIGNMENT,
                    font=FONT)

    def game_over(self):
        self.goto(0, 0)
        # self.color()
        self.write ("Game Over",
                    move=False,
                    align=ALIGNMENT,
                    font=FONT)
    def score_refresh(self):
        self.clear()
        self.score += 1
        self.update_score()


    def g_high_score(self):
        if self.score > self.high_score :
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_score()











