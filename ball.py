from turtle import Turtle

class Ball(Turtle):

    BALL_STEP = 10
    STARTING_SPEED = 0.05
    SPEED_INCREASE = 0.9

    def __init__(self):
        super().__init__()
        self.shape(name="circle")
        self.color("white")
        self.penup()
        self.move_x = Ball.BALL_STEP
        self.move_y = Ball.BALL_STEP
        self.ball_speed = Ball.STARTING_SPEED


    def move(self):
        new_x = self.xcor() + self.move_x
        # print(new_x, type(new_x))
        new_y = self.ycor() + self.move_y
        self.goto(new_x,new_y)

    
    def bounce_y(self):
        self.move_y *= -1


    def bounce_x(self):
        self.move_x *= -1
        self.ball_speed *= Ball.SPEED_INCREASE

    def reset_ball(self):
        
        self.goto(0,0)
        self.ball_speed = Ball.STARTING_SPEED
        self.bounce_x()