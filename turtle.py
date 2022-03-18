#noela created turtle.py
import turtle
window=turtle.Screen()
window.bgcolor("blue")
window.title("5-sided star")

alex=turtle.Turtle()
alex.color("pink")

alex.pensize(11)
def mov(angle,distance):
    alex.penup()
    alex.right(angle)
    alex.forward(distance)
    alex.left(angle)
    alex.pendown()

alex.penup()
alex.left(135)
alex.forward(177)
alex.right(135)
alex.pendown()

for i in range(3):
    alex.forward(200)
    alex.left(120)
mov(0,250)
for i in range(4):
    alex.forward(100)
    alex.left(90)
mov(90,300)
for i in range(6):
    alex.forward(100)
    alex.left(60)
mov(180,300)
for i in range(8):
    alex.forward(100)
    alex.left(45)
window.mainloop()
