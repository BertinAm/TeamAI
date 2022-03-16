import turtle
window=turtle.Screen()
window.bgcolor("blue")
window.title("hello")

alex=turtle.Turtle()
alex.color("pink")

alex.pensize(5)
for i in range(10):
alex.forward(80)
alex.left(72)
alex.forward(80)
alex.left(72)
window.mainloop()
