from turtle import Turtle

class Snake(Turtle):
    def __init__(self, shape: str = "square") -> None:
        super().__init__(shape)
        self.shapesize(2, 2, 1)
        self.penup()
        self.color("white")
        self.speed(1)