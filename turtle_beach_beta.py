objects.setx(x - 20)

y = objects.ycor()
objects.sety(y + 30)

new = Turtle()

y = new.ycor()
new.sety(y - 40)

new.shape("turtle")
new.penup()

screen.listen()

screen.onkey(move_new_forward, "Up")
screen.onkey(move_new_backward, "Down")
screen.onkey(move_new_left, "Left")
screen.onkey(move_new_right, "Right")
screen.onkey(restart, 'r')

screen.mainloop()

screen = True
