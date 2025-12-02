from turtle import Turtle

class Paddle(Turtle):

    STEP = 20
    LIMIT = 430
    WIDTH = 6
    LENGTH = 1


    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=Paddle.WIDTH, stretch_len=Paddle.LENGTH)
        self.penup()
        self.goto(position)


    def go_up(self):
        new_y = self.ycor() + Paddle.STEP
        if new_y < Paddle.LIMIT:            #420
            self.goto(self.xcor(), new_y)


    def go_down(self):
        new_y = self.ycor() - Paddle.STEP
        if new_y > -Paddle.LIMIT:           # -420
            self.goto(self.xcor(), new_y)
