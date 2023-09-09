from turtle import Screen
from snake import Snake
from food import Food
from scorecard import ScoreCard
import time
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scorecard = ScoreCard()
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")



is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect collison with food
    if snake.head.distance(food) < 15:
        scorecard.increase_score()
        snake.extend()
        food.refresh()
        print("nom nom nom")
    #detect collison with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.xcor()<-280:
        is_game_on = False
        scorecard.game_over()

    #detect collison with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scorecard.game_over()






screen.exitonclick()

