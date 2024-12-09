from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# UI setup using imported classes from turtle graphics library
# creates objects & initializes classes
screen = Screen()
t = Turtle()
snake = Snake()
food = Food()
score = Scoreboard()

# screen/window setup & turns off tracer(animations) method in screen class
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Snaky Snaky")
screen.tracer(0)

# screen object listens for certain keystrokes
screen.listen()
# specifying & binding keystrokes to commands from snake object
screen.onkey(snake.up, key="Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.left, key="Left")
screen.onkey(snake.right, key="Right")

food.create_food()
score.create_score()

# variable set to true to be used for while loop
game_is_on = True

# while loop to continuously loop if variable is = to TRUE
while game_is_on:
    # refreshes graphic's on screen
    screen.update()
    # sleeps (delays) for 0.1 seconds
    time.sleep(0.1)
    # moves snake, after screen update & sleep very quickly to hide animation but also move snake
    snake.move()

    # detect collision with food
    # checks distance from snake head to food if less than 19 pixels,
    # calls food to refresh ,snake to extend & updates the score +1
    if snake.head.distance(food) < 19:
        food.refresh()
        snake.extend()
        score.refresh_score()

    # detect collision with wall
    # checks distance from snake-head's x & y coordinate to the wall if greater/less than 380-400px(the wall/screen)
    # if so calls snake.reset & score.reset
    if snake.head.xcor() > 390 or snake.head.xcor() < -400 or snake.head.ycor() > 400 or snake.head.ycor() < -390:
        snake.reset()
        score.reset()

    # detect collision with tail of snake
    for x in snake.snake_list:
        if x == snake.head:
            pass
        # if snake head is in range of coordinates of snake_list(snakes body/ squares) then execute reset
        elif snake.head.distance(x) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
