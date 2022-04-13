import random
import time
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

START_POSITION = 320
END_POSITION = -320

class CarManager():

    def __init__(self):
        self.all_cars = []
        self.car_speed = 5

    def create_cars(self):
        if random.randrange(1, 6) != 3:
            return
        car = Turtle(shape="square")
        car.shapesize(1, 2)
        car.color(random.choice(COLORS))
        pos_y = random.randrange(280, -200, -20)
        car.penup()
        car.goto(START_POSITION, pos_y)
        car.setheading(0)
        car.pendown()
        self.all_cars.append(car)

    def start_engine(self):
        for car in self.all_cars:
            if car.xcor() >= END_POSITION:
                car.penup()
                car.backward(self.car_speed)
                car.pendown()
            else:
                car.hideturtle()

    def level_up(self):
        self.car_speed += MOVE_INCREMENT