import turtle
from snake import Snake
import time
import food
from scoreboard import ScoreBoard
from tkinter import messagebox
from turtle import Screen, Turtle


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
            screen.update()
            if messagebox.askretrycancel(title='Game Over', message='Out of Bounds'):
                score_board.sethigh_score()
                snake.reset_snake()
            else:
                screen.bye()
        if snake.collided():
            screen.update()
            if messagebox.askretrycancel(title='Game Over', message='Collided'):
                score_board.sethigh_score()
                snake.reset_snake()
            else:
                screen.bye()

    screen.exitonclick()


def main_menu():
    screen = Screen()

    def on_press():
        startup_text.clear()
        screen.clear()
        main()
    screen.bgcolor('black')
    screen.tracer(0)
    screen.onkey(on_press, "Return")
    screen.listen()
    startup_text = Turtle()
    startup_text.color('white')
    startup_text.penup()
    startup_text.hideturtle()
    startup_text.goto(0, 0)
    startup_text.write("Press Enter to Start", True, align='center', font=("Arial", 25, "normal"))
    screen.update()
    screen.exitonclick()


main_menu()
