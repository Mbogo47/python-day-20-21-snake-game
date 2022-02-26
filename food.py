from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        """Creates the snake's food"""
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=.5 ,stretch_wid=.5)
        self.color("gold")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Creates snake food at a random place"""
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 280)
        self.goto(new_x, new_y)

    