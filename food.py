from turtle import Turtle
from random import *


# renders food for snake to eat on screen in random location
class Food(Turtle):

    def __init__(self):
        super().__init__()

    # creates circle shape for food
    # colors & place's it at random coordinate -380 & 380 for x and y on the screen
    def create_food(self):
        self.penup()
        self.shape("turtle")
        self.shapesize(0.8, 0.8)
        self.speed("fastest")
        self.color("yellow")
        y = randint(-380, 380)
        x = randint(-380, 380)
        self.goto(x=x, y=y)

    # clears & calls create_food() again to redeploy new food at random location
    def refresh(self):
        self.clear()
        self.create_food()
