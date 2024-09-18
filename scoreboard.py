from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.goto(0,280)
        self.color("blue")
        self.hideturtle()
        self.update()
    def update(self):
        self.write(f"Score: {self.score}")
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER")

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update()
