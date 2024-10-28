import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Side length
side_length = 100

# Draw a square
from figures import draw_square
draw_square(side_length)

# Hide the turtle and finish
window.mainloop()