from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


# Scoreboard class that inherits from Turtle class and creates a scoreboard object
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0  # Initialize the score to 0
        self.penup()
        self.hideturtle()  # Hide the turtle
        self.color("white")
        self.goto(0, 260)  # Set the position of the scoreboard object
        self.write(f"Score: {self.score}", align="center", font=FONT)  # Write the score on the screen

    # Method to increase the score by 1
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=FONT)  # Write the updated score on the screen

    # Method to display the game over message
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
