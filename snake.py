from turtle import Turtle, Screen

screen = Screen()  # Create a screen object
screen.register_shape("scared.gif")  # Register the image file for the snake object
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# Snake class that creates a snake object
class Snake:
    def __init__(self):
        self.segments = []  # Initialize the segments list
        self.create_snake()  # Call the create_snake method
        self.head = self.segments[0]  # Set the head of the snake object

    # Method to create the snake object
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # Method to add a segment to the snake object
    def add_segment(self, position):
        new_turtle = Turtle("scared.gif")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    # Method to extend the snake object
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Method to move the snake object
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    # Method to move the snake object up, down, left, or right
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
