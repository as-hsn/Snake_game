from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

# Set up the screen
screen = Screen ()
screen.tracer (0)
screen.setup (height=600,
              width=600)
screen.bgcolor ("black")
screen.title ("Snake Game")

# Initialize the snake positions

snake = Snake()
food = Food()
score = ScoreBoard()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.listen()
    screen.onkeypress(snake.up,
                       "Up")
    screen.onkeypress(snake.down,
                       "Down")
    screen.onkeypress(snake.left,
                       "Left")
    screen.onkeypress(snake.right,
                       "Right")

    # Detect collision and with food.
    if snake.head.distance(food) < 15:
        snake.update_snake()
        food.refresh()
        score.score_refresh()

    # snake collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor () > 280 or snake.head.ycor () < -300 :
        snake.snake_refresh()
        score.g_high_score()

    # Detect collision with tail.

    for call in snake.snakes[1 :] :
        if snake.head.distance (call) < 10 :
            snake.snake_refresh ()

# Close the game window when the game ends
screen.exitonclick()
