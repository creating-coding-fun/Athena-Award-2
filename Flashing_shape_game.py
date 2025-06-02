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
        pen.goto(x, y - 60)
        pen.pendown()
        pen.circle(60)
    elif shape == "square":
        pen.goto(x - 50, y - 50)
        pen.pendown()
        for i in range(4):
            pen.forward(100)
            pen.left(90)
    elif shape == "triangle":
        pen.goto(x - 50, y - 30)
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

    pen.clear()
    screen.update()
    time.sleep(0.2)


def preview_shapes():
    pen.clear()
    screen.tracer(1)
    time.sleep(1)

    for shape in shapes:
        pen.clear()
        x, y = shapes_positions[shape]
        drawing_shape(shape, x, y, "white")
        time.sleep(1.5)

    pen.clear()
    time.sleep(0.5)

    
def flash_sequence():
    preview_shapes()
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
    pen.penup()
    pen.goto(0, -100)
    pen.write(f"Your answer, {typed_input}", align = "center", font=("Arial", 16, "normal"))
    pen.goto(0, -150)  
    pen.write(f"Correct sequence, {sequence}", align = "center", font=("Arial", 16, "normal"))
    if typed_input == sequence:
        screen.textinput("Result", "Yaaay! You are correct! :D Press esc to exit!")
    else:
        screen.textinput("Result", "Oop...I guess you couldn't remember :/..press esc to exit.")
    turtle.bye()


flash_sequence()
screen.ontimer(handling_input, 500)

screen.mainloop()      


    







