# trying inta code




def Cppsecrets(python, cplusplus):
    if python > 0:
        turtle.forward(python)
        turtle.right(cplusplus)
        Cppsecrets(python-5, cplusplus)


from random import Random
import turtle
turtle.shape('turtle')
turtle.reset()
turtle.speed(0)
turtle.pen(speed=1)
turtle.bgcolor("black")
turtle.color("white")
turtle.delay(0)
length =600
turn_by=121
turtle.penup()
turtle.setpos(-length/2,length/2)
turtle.pendown()
Cppsecrets(length,turn_by)
