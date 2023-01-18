import turtle as t
import random
import time
  
        
t.bgcolor("lightgreen")
t.setup(500,700)

#플레이어(ball)
ball=t.Turtle()
ball.shape("circle")
ball.shapesize(1.1)
ball.up()
ball.speed(0)
ball.color("white")
ball.goto(-190,-135)
