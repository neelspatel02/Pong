from turtle import Screen
from paddle import Paddle
from ball import Ball 
from scoreboard import Scoreboard 
import time
from game_menu import Menu

# screen borders
Y_EDGE = 480
X_EDGE = 880


menu = Menu()
mode, difficulty = menu.user_input()

mode = mode.lower()
difficulty = difficulty.lower()
# print(mode, difficulty)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1800, height=1000)
screen.title(f"Pong: {mode}")
screen.tracer(0)

r_paddle = Paddle((850,0))
l_paddle = Paddle((-850,0))
ball = Ball()
scoreboard = Scoreboard()



if difficulty == "easy":
        ai_speed = 4

elif difficulty == "medium":
        ai_speed = 8

elif difficulty == "hard":
        ai_speed = 12

else:
        ai_speed = 6


screen.listen()


if mode == "double_player":

        screen.onkey(r_paddle.go_up, "Up")
        screen.onkey(r_paddle.go_down, "Down")

        screen.onkey(l_paddle.go_up, "w")
        screen.onkey(l_paddle.go_down, "s")

else:
        screen.onkey(r_paddle.go_up, "Up")
        screen.onkey(r_paddle.go_down, "Down")


game_on = True
# hit = True
while game_on:
        time.sleep(ball.ball_speed)
        screen.update()

        if mode == "single_player":

                if l_paddle.ycor() < ball.ycor():
                        l_paddle.sety(l_paddle.ycor() + ai_speed)

                elif l_paddle.ycor() > ball.ycor():
                        l_paddle.sety(l_paddle.ycor() - ai_speed)

        ball.move()

        if ball.ycor() > Y_EDGE or ball.ycor() < -Y_EDGE:
                ball.bounce_y()


        if ball.xcor() > 870:
                scoreboard.left_point()
                ball.reset_ball()
                continue
        
        if ball.xcor() < -870:
                scoreboard.right_point()
                ball.reset_ball()
                continue
        
        if 820 < ball.xcor() < 850 and abs(ball.ycor() - r_paddle.ycor()) < 60:
                ball.bounce_x()


        if -850 < ball.xcor() < -820 and abs(ball.ycor() - l_paddle.ycor()) < 60:
                ball.bounce_x()

screen.exitonclick()


        # if ((ball.distance(r_paddle) < 60 and ball.xcor() > 820) or \
        #         (ball.distance(l_paddle) < 60 and ball.xcor() < -820)):
        #         ball.bounce_x()

        #         # hit = False


        # if ball.xcor() > 870:
        #         ball.reset_ball()

        # if ball.xcor() < -870:
        #         ball.reset_ball()
