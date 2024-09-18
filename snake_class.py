from turtle import Turtle,Screen
screen=Screen()


starting_position=[(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()

    def create_snake(self):
        for position in starting_position:
            tim = Turtle()
            tim.shape("square")
            tim.penup()
            tim.goto(position)
            self.segments.append(tim)
    def add_segment(self):
        tim = Turtle()
        tim.shape("square")
        tim.penup()
        x=self.segments[-1].xcor()
        y=self.segments[-1].ycor()
        tim.goto(x,y)
        self.segments.append(tim)






    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[i - 1].xcor()
            y_cor = self.segments[i - 1].ycor()
            self.segments[i].goto(x_cor, y_cor)
        self.segments[0].forward(20)
    def up(self):
        if self.segments[0].heading()!=270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading()!=90:
            self.segments[0].setheading(270)
    def left(self):
        if self.segments[0].heading()!=0:
            self.segments[0].setheading(180)
    def right(self):
        if self.segments[0].heading()!=180:
            self.segments[0].setheading(0)

