'''
color list:
red
orange
yellow
green
blue
indigo
purple
'''
import turtle

#
def picture(pic_path,pic_x,pic_y):
    screen = turtle.Screen()
    screen.register_shape(pic_path)
    envelope = turtle.Turtle(pic_path)
    envelope.penup()
    envelope.goto(pic_x, pic_y)
    envelope.stamp()
    envelope.hideturtle()

def happy_new_year():
    picture("red-envelope.gif",-250,-200)
    picture("2021.gif",250,-200)

# 畫鼻子
def drawNose():
    turtle.penup()
    turtle.seth(90)
    turtle.fd(100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('black')
    turtle.seth(45)
    turtle.fd(25)
    turtle.seth(135)
    turtle.circle(25, 95)
    turtle.seth(315)
    turtle.fd(25)
    turtle.end_fill()


# 畫眼睛
def drawEyes(seth, fd, r):
    turtle.penup()
    turtle.seth(seth)
    turtle.fd(fd)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('black')
    turtle.circle(50)
    turtle.end_fill()
    turtle.penup()
    turtle.circle(50, r)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('white')
    turtle.circle(20)
    turtle.end_fill()


# 畫臉
def drawFace(seth, fd):
    turtle.penup()
    turtle.seth(seth)
    turtle.fd(fd)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('red')
    turtle.circle(70)
    turtle.end_fill()


# 畫嘴巴
def drawLip():
    turtle.penup()
    turtle.seth(135)
    turtle.fd(250)
    turtle.pendown()
    turtle.seth(-300)
    turtle.circle(30, -65)
    turtle.begin_fill()
    turtle.fillcolor('Firebrick')
    turtle.seth(165)
    turtle.fd(140)
    turtle.seth(195)
    turtle.fd(140)
    turtle.seth(-360)
    turtle.circle(30, -65)
    turtle.penup()
    turtle.seth(-60)
    turtle.circle(30, 65)
    turtle.pendown()
    turtle.seth(-70)
    turtle.fd(240)
    turtle.circle(55, 140)
    turtle.seth(70)
    turtle.fd(240)
    turtle.end_fill()
    turtle.seth(-110)
    turtle.fd(80)
    turtle.seth(120)
    turtle.circle(120, 123)



def pikachu(color="pink",pensize=4, speed=20):
    turtle.pensize(pensize)
    turtle.hideturtle()
    turtle.setup(1000, 600)
    turtle.speed(speed)
    turtle.screensize(bg=color)
    drawNose()
    drawEyes(160, 250, 60)
    drawEyes(-9.5, 530, 230)
    drawFace(195, 600)
    drawFace(-11, 720)
    drawLip()

def finish():
    turtle.done()
    turtle.bye()

