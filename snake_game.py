import turtle
from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")

# turn off the turtle animation
screen.tracer(0)
scoreboard = Score()

snake = Snake()
food = Food()

# TODO: 3. control the snake (up, left, down, right) arrow keys
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # TODO: 4. detect collision with food
    # distance method
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        # TODO: 5. Create a scoreboard
        scoreboard.increase_score()

    # TODO: 6. detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()

    # TODO: 7. Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()
