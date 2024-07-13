from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# Create the snake, food, and scoreboard objects
snake = Snake()
food = Food()
write = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # Update the screen and move the snake object
    screen.update()
    # Pause the program for 0.1 seconds to slow down the snake object
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:  # Check if the snake object has collided with the food object
        food.refresh()
        write.increase_score()
        snake.extend()
    # Check if the snake object has collided with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            write.game_over()
    # Check if the snake object has collided with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        write.game_over()

screen.exitonclick()
