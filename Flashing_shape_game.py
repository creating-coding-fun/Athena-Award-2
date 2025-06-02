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

colors = ["pink", "blue", "yellow", "orange", "purple", "red", "magenta", "green"]
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
    color = random.choice(colors)
    x, y = shapes_positions [shape]
    drawing_shape(shape, x, y, color)
    time.sleep(0.5)
    drawing_shape(shape, x, y, color)
    time.sleep(0.3)

    pen.clear()
    screen.update()
    time.sleep(0.2)

def ready_set_go ():
    pen.penup()
    pen.goto(0, 0)
    pen.color(random.choice(colors))
    pen.write("Ready?", align = "center", font=("Inconsolata", 50, "bold"))
    time.sleep(1)
    pen.clear()
    pen.penup()
    pen.goto(0, 0)
    pen.color(random.choice(colors))
    pen.write("Set!", align = "center", font=("Inconsolata", 50, "bold"))
    time.sleep(1)
    pen.clear()
    pen.penup()
    pen.goto(0, 0)
    pen.color(random.choice(colors))
    pen.write("Go!!", align = "center", font=("Inconsolata", 50, "bold"))
    time.sleep(1)
    pen.clear()


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
    ready_set_go()
    screen.tracer(1)
    time.sleep(1)

    for i in range(5):
        shape = random.choice(shapes)
        sequence.append(shape)
        flash_shape(shape)
        time.sleep(0.5)
        pen.penup()
        pen.goto(0,0)
    pen.write("Shape sequence has been shown!! Type it in now:", align = "center", font=("Inconsolata", 16, "normal"))
    time.sleep(1)

def handling_input():
    global user_input
    user_input = screen.textinput("Memory Challenge", "Your Answer: Type it in now >:), type it as a list without commas. (eg. circle square triangle circle square)")
    check_input()

def check_input():
    global current_round, total_rounds
    typed_input = user_input.strip().lower().split()
    pen.penup()
    pen.goto(0, -100)
    pen.write(f"Your answer, {typed_input}", align = "center", font=("Inconsolata", 16, "normal"))
    pen.goto(0, -150)  
    pen.write(f"Correct sequence, {sequence}", align = "center", font=("Inconsolata", 16, "bold"))
    if typed_input == sequence:
        pen.goto(0, -200)
        pen.write("Yay that was correct! You memory master!!", align = "center", font=("Inconsolata", 20, "normal"))
        current_round += 1
        if current_round <= total_rounds:
            time.sleep(2)
            pen.clear()
            start_rounds()
        else:
            time.sleep(2)
            pen.goto(0, 0)
            pen.write("YESS YOU WON THE GAME!!", align = "center", font=("Inconsolata", 20, "bold"))
            time.sleep(3)
            turtle.bye()
    else:
        pen.goto(0, 100)
        pen.write( "Oop...I guess you couldn't remember :/...Game Over", align = "center", font=("Inconsolata", 20, "normal"))
        time.sleep(4)
        turtle.bye()

    current_round = 1
    total_rounds = 1

def play_rounds():
    while True:
        rounds = screen.textinput("Rounds", "How many rounds would you like to play?")
        if rounds and rounds.isdigit():
            rounds = int(rounds)
            if rounds <= 0:
                screen.textinput("Rounds", "Invalid input! Try again!")
                continue
            else:
                return rounds
        else:
            screen.textinput("Rounds", "Please enter a valid number of rounds! It ain't that hard.")

def game():
    global current_round, total_rounds
    total_rounds = play_rounds()
    current_round = 1
    start_rounds()

def start_rounds():
    global current_round
    if current_round <= total_rounds:
        sequence.clear
        pen.clear()
        pen.penup()
        pen.goto(0, 250)
        pen.write(f"Round, {current_round} out of {total_rounds}", align = "center", font=("Arial", 20, "bold"))
        time.sleep(2)
        flash_sequence()
        screen.ontimer(handling_input, 500)
    else: 
        pen.clear()
        pen.penup()
        pen.goto(0, 0)
        pen.write("Yay you have completed all the rounds of the game!!", align = "center", font=("Arial", 20, "bold"))



    


game()
screen.mainloop()      


    







