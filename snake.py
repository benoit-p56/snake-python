from turtle import Turtle

class Snake(Turtle):
    def __init__(self, shape: str = "square") -> None:
        super().__init__(shape)
        self.shapesize(3, 3, 1)
        self.penup()
        self.color("white")
        self.speed(0)
    
    def m_up(self):
        self.setheading(90)
    def m_down(self):
        self.setheading(270)
    def m_left(self):
        self.setheading(180)
    def m_right(self):
        self.setheading(0)

    