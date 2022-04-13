"""
    1. A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.
"""
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player (Turtle):

    def __init__(self):
        super().__init__(shape="turtle")
        self.color("green")
        self.go_to_start()

    def move(self):
        self.penup()
        self.forward(MOVE_DISTANCE)
        self.pendown()

    def is_at_finish_line(self):
        return self.ycor() == FINISH_LINE_Y

    def go_to_start(self):
        self.penup()
        self.goto(STARTING_POSITION)
        self.pendown()
        self.setheading(90)
