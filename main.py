import turtle
from snake import Snake
import time
import food
from scoreboard import ScoreBoard
from tkinter import messagebox


def main():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.title('Snake Game')
    screen.bgcolor('black')
    screen.tracer(100)
    snake = Snake()
    snack = food.Food()
    score_board = ScoreBoard()

    screen.onkey(snake.move_up, "w")
    screen.onkey(snake.move_left, "a")
    screen.onkey(snake.move_right, "d")
    screen.onkey(snake.move_down, "s")
    screen.listen()

    running = True
    while running:

        screen.update()
        time.sleep(0.1)
        if snake.head.distance(snack.food) < 15:
            score_board.clear()
            snack.change_position()
            score_board.change_score()
            snake.add_snake()
        snake.move()
        if snake.head.ycor() >= 310 or snake.head.ycor() <= -290 or snake.head.xcor() >= 290 or snake.head.xcor() <= -290:
            if messagebox.askretrycancel(f"Score: {score_board.score}", "You have gone out of Bounds...Try again?"):
                screen.reset()
                main()
            else:
                screen.bye()
        if snake.collided():
            if messagebox.askretrycancel(f"Score: {score_board.score}", "You have collided with your self..Try again?"):
                screen.reset()
                main()
            else:
                screen.bye()

    screen.exitonclick()


main()
