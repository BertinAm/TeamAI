#Noela completed drunkman
import turtle
window=turtle.Screen()
window.title("drunkman")
window.bgcolor("pink")
alex=turtle.Turtle()
alex.pensize(5)
alex.color("black")
angle=[160,317,270,253,317,200,140,17,274]
for i in angle:
    alex.left(i)
    alex.forward(40)
alex.forward(100)
for i in angle:
    alex.left(i)
    alex.forward(40)
alex.forward(100)
window.mainloop()

