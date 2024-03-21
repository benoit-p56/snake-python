import turtle as t

class Snake():
    snake = t.Turtle()
    snake.shapesize(2, 2, 1)
    snake.penup()
    snake.shape("square")
    snake.color("white")
    snake.speed(1)