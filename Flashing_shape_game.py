import turtle
import time
import random

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Memory Challenge Game")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

shapes = ["circle", "square", "triangle"]
sequence = []
user_sequence = []

shapes_positions = {"circle": (0, 0), "square": (0, 0), "triangle": (0, 0)}

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
    time.sleep(0.3)

def show_shapes():
    pen.clear()
    for shape in shapes:
        drawing_shape(shape, *shapes_positions[shape])
        screen.update()

    
def flash_sequence():
    screen.tracer(0)
    show_shapes()
    screen.tracer(1)
    time.sleep(1)

    for i in range(5):
        shape = random.choice(shapes)
        sequence.append(shape)
        flash_shape(shape)
    print("Shape sequence has been shown!! Type it in now (eg. circle, triangle, square, triangle, circle)")

def handling_input():
    global user_input
    user_input = screen.textinput("Memory Challenge", "Your Answer: Type it in now >:)")
    check_input()

def check_input():
    typed_input = user_input.strip().lower().split()
    screen.text(f"Your answer, {typed_input}")
    screen.text(f"Correct sequence, {sequence}")
    if typed_input == sequence:
        screen.textinput("Result", "Yaaay! You are correct! :D Press esc to exit!")
    else:
        screen.textinput("Result", "Oop...I guess you couldn't remember :/..press esc to exit.")
    turtle.bye()

flash_sequence()
screen.ontimer(handling_input, 500)

screen.mainloop()    


    







