import turtle 
#turtle.setworldcoordinates(1, -5000, 30, 30)

def Hilbert(length, myTurtle):
    myTurtle.forward(length)
    myTurtle.right(90)
    myTurtle.forward(length)
    myTurtle.right(90)
    myTurtle.forward(length)
    myTurtle.left(90)
    myTurtle.forward(length)
    myTurtle.forward(length) #right, right, left

    myTurtle.left(90)
    myTurtle.forward(length)
    myTurtle.left(90)
    myTurtle.forward(length)
    myTurtle.right(90)
    myTurtle.forward(length) #left, left, right, right, left, left
    myTurtle.right(90)
    myTurtle.forward(length)
    myTurtle.left(90)
    myTurtle.forward(length)
    myTurtle.left(90)
    myTurtle.forward(length)
    myTurtle.forward(length) 
    
    myTurtle.left(90)
    myTurtle.forward(length)
    myTurtle.right(90)
    myTurtle.forward(length)
    myTurtle.right(90)
    myTurtle.forward(length)
    myTurtle.forward(length) #left, right,              right, right, left, left
    myTurtle.right(90)
    myTurtle.forward(length)
    myTurtle.left(90)
    myTurtle.forward(length)
    myTurtle.left(90)
    myTurtle.forward(length)
    myTurtle.right(90)
    myTurtle.forward(length)
    myTurtle.forward(length) 

    myTurtle.right(90)
    myTurtle.forward(length)
    myTurtle.right(90)
    myTurtle.forward(length)
    myTurtle.left(90)
    myTurtle.forward(length)
    myTurtle.left(90)
    myTurtle.forward(length) #right, right, left, left, right, right
    myTurtle.right(90)
    myTurtle.forward(length)
    myTurtle.right(90)
    myTurtle.forward(length)
    myTurtle.forward(length)

    myTurtle.right(90)
    myTurtle.forward(length)
    myTurtle.left(90)
    myTurtle.forward(length)
    myTurtle.left(90)
    myTurtle.forward(length)
    myTurtle.forward(length)
    myTurtle.forward(length)
    myTurtle.left(90)
    myTurtle.forward(length) #right, left, left, left, left, right, 
    myTurtle.left(90)
    myTurtle.forward(length)
    myTurtle.right(90)
    myTurtle.forward(length)
    myTurtle.forward(length)




def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    Hilbert(5, myTurtle)    
    myWin.exitonclick()

main()