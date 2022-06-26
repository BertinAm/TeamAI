import turtle
window=turtle.Screen()
window.bgcolor("blue")
window.title("5-sided star")

alex=turtle.Turtle()
alex.color("pink")

alex.pensize(11)
for i in range(5):
    alex.forward(100)
    alex.left(72)
    alex.forward(100)
    alex.right(144)

window.mainloop()
