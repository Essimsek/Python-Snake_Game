from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

# Set up
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Objects
score = Score()
snake = Snake()
food = Food()

# Handling the key events
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Escape", fun=screen.bye)

while True:

	screen.update()
	time.sleep(0.1)
	snake.move()

	if snake.segments[0].distance(food) < 15:
		score.update_score()
		score.write_score()
		snake.extend()
		food.generate_new_food()

	if snake.check_collision() or snake.check_tail_collision():
		score.reset_scoreboard()
		snake.reset_snake()

screen.exitonclick()

