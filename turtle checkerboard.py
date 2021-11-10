import turtle
tracy = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Make your own Checkerboard")
turtle.speed(0)
screen = turtle.Screen
answer = True
def square(length, width):
    turtle.begin_fill()
    for i in range (2):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()
def next_square(length):
    turtle.penup()
    turtle.forward(length)
    turtle.pendown()

def move_up_a_row(a):
    y=turtle.ycor()
    turtle.penup()
    turtle.goto(-200,y+a)
    turtle.pendown()

while True:
    answer = True
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200,-200)
    rows = turtle.numinput("Rows" , "How many rows? ")
    columns = turtle.numinput("Columns" , "How many columns? ")

    for row in range(int(rows)):
        for column in range(int(columns)):
            if (row+column) % 2 == 0:
                turtle.color("red")
            else:
                turtle.color("black")
            square(400.0/columns, 400.0/rows)
            next_square(400.0/columns)
        move_up_a_row(400.0/rows)
    answer = turtle.textinput("Pattern finished" , "Do you wish to repeat? ")
    if answer == "yes":
        answer = True
        turtle.reset()
    else:
        turtle.bye()
