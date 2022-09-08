import turtle
import random


t = turtle.Turtle()
w = turtle.Screen()

color = ['yellow', 'red', 'green', 'cyan', 'blue', 'brown', 'white', 'lemonchiffon', 'midnightblue', 'deeppink']
t.speed(10000)

w.bgcolor("midnightblue")

t.color("white")

w.title("Trung Thu Zui Ze")

#create small_star
def stars():
    t.pencolor(color[0])
    for i in range(5):
        t.fd(10)
        t.right(144)

#create moon_circle
def moon():
    t.speed(5)
    t.up()
    t.goto(400, 170)
    t.down()
    t.color(color[7])
    t.begin_fill()
    t.circle(80)
    t.end_fill()
    t.hideturtle()


#create random stars
def random_star():

    for i in range(100):
        x = random.randint(-640, 640)
        y = random.randint(-330, 330)
        stars()
        t.up()
        t.goto(x, y)
        t.down()

#create star_lantern
def big_star():
    t.speed(10)
    t.pensize(10)
    t.penup()
    t.setpos(-90, 30)
    t.pendown()
    t.pencolor(color[0])
    for i in range(5):
        t.forward(200)
        t.right(144)


#star_lantern frame
def frame():

    t.pensize(5)
    t.pencolor(color[1])

    t.penup()
    t.setpos(10, 106)
    t.pendown()
    t.goto(115,30)

    t.penup()
    t.setpos(115, 30)
    t.pendown()
    t.goto(75,-90)

    t.penup()
    t.setpos(75, -90)
    t.pendown()
    t.goto(-53,-90)

    t.penup()
    t.setpos(-53, -90)
    t.pendown()
    t.goto(-95, 30)

    t.penup()
    t.setpos(-95, 30)
    t.pendown()
    t.goto(10, 106)

def taycam():
    # tay cam
    t.penup()
    t.setpos(80, -140)
    t.pensize(10)
    t.pencolor(color[5])
    t.penup()
    t.goto(-195, 105)
    t.pendown()
    t.forward(201)

def print_text():
    t.color('cyan')
    style = ('Courier', 30, 'bold')
    t.penup()
    # t.pendown()
    t.goto(-300, -300)
    t.write('CHÚC CÁC BÉ TRUNG THU VUI VẺ!!!', font=style)
    t.hideturtle()

if __name__ == '__main__':
    random_star()
    moon()
    big_star()
    frame()
    taycam()
    print_text()
    w.exitonclick()


