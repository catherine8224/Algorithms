import turtle
import random

r = random.randrange(15,26)

branchlen = random.randrange(10,30)

def tree(branchLen,t, p):
    if branchLen > 5:
        if branchLen <= 15:
            t.color("green", "dark green")
        #else:
        #    t.color("brown")
        t.pensize(p)
        t.forward(branchLen)
        t.right(20) #20
        tree(branchLen-15,t, p-2)
        t.left(40) #40
        tree(branchLen-15,t, p-2)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    t.pensize(10)
    tree(75,t, 10)
    myWin.exitonclick()

main()