import turtle
import random


class Food(object):
    def __init__(self):
        self.food = turtle.Turtle(shape='circle')
        self.food.penup()
        self.food.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.food.color('lime')
        self.change_position()

    def change_position(self):
        self.food.goto(random.randint(40, 260), random.randint(40, 260))
