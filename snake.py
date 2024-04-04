from turtle import Turtle

class Snake(Turtle):
    def __init__(self, shape: str = "square") -> None:
        super().__init__(shape)
        self.shapesize(3, 3, 1)
        self.penup()
        self.color("white")
        self.speed(1)