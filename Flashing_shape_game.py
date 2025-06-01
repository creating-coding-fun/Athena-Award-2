import turtle
import time
import random

screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.title("Memory Challenge Game")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed()

shapes = ["circe", "square", "triangle"]
sequence = []
user_sequence = []

shapes_positions = {"circle: (-100, 0), square: (0, 0), triangel: (100, 0)"}

def drawing_shape (shape, x,y, color="white"):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    if shape == "circle":
        pen.circle(60)
    elif shape == "square":
        for i in range(4):
            pen.forward(100)
            pen.right(90)
    elif shape == "triangle":
        for i in range(3):
            pen.forward(100)
            pen.left(120)
    pen.end_fill()
    screen.update()

    def flash_shape(shape):
        x, y = shapes_positions [shape]
        drawing_shape(shape, x, y, "blue")
        time.sleep(0.5)
        drawing_shape(shape, x, y, "green")
        time.sleep(0.5)
    
    def show_shapes():
        pen.clear()
        for shape in shapes:
            drawing_shape(shape *shapes_positions[shape])
            screen.update

    
    def flash_sequence():
        screen.tracer(0)
        show_shapes()
        screen.tracer(1)
        time.sleep(1)

        for i in range(5):
            shape = random.choice(shapes)
            sequence.append[shape]
            flash_shape(shape)
        print("Shape sequence has been shown!! Type it in now (eg. circle, triangle, square, triangle, circle)")

  


    







