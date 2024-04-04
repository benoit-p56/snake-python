import turtle as t
import snake

screen = t.Screen()
screen.bgcolor("black")
screen.setup(1000, 800)
s = snake.Snake() 

gaming = True

x_border = (screen.window_width()/2) - 40
y_border = (screen.window_height()/2) - 35
s.setheading(180)

while gaming:
    if s.xcor() in [x_border*-1 - 10, x_border] or s.ycor() in [ y_border*-1, y_border]:
        gaming = False
    s.forward(5)



screen.exitonclick()
