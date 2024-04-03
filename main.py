import turtle as t
import snake

screen = t.Screen()
screen.bgcolor("black")
screen.setup(1000, 800)
s = snake.Snake() 

gaming = True

x_border = (screen.window_width()/2) - 30
y_border = (screen.window_height()/2) - 30

while gaming:
    if s.xcor() in [x_border, x_border*-1] or s.ycor() in [y_border, y_border*-1]:
        gaming = False
    s.forward(5)



screen.exitonclick()
