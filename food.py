from turtle import Turtle, Screen
from random import Random

screen = Screen()
screen.register_shape("boiled-egg.gif")  # Register the image file


# Food class that inherits from Turtle class and creates a food object
class Food(Turtle):
    def __init__(self):
        super().__init__()      # Call the Turtle class constructor
        self.shape("boiled-egg.gif")    # Set the shape of the food object to the image file
        self.penup()
        self.speed("fastest")
        self.goto(Random().randint(-280, 280), Random().randint(-280, 280)) # Set the initial position of the food object
        self.refresh()  # Call the refresh method

    # Method to refresh the position of the food object
    def refresh(self):
        self.goto(Random().randint(-280, 280), Random().randint(-280, 280))
