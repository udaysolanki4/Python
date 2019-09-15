
import turtle

# Your code here.
def draw_square(some_turtle):
    while True:
        for i in range(1,5):
            some_turtle.forward(100)
            some_turtle.right(90)
##            some_turtle.right(60)
##            some_turtle.forward(100)
##            some_turtle.right(120)
        some_turtle.right(6)
    
def draw_art():
    window = turtle.Screen()
    window.bgcolor("grey")

    yu = turtle.Turtle()
    yu.shape("turtle")
    yu.color("white")
    yu.speed(0)
    
    
    draw_square( yu )
    

##    yu1 = turtle.Turtle()
##    yu1.shape("arrow")
##    yu1.color("black")
##    yu1.circle(50)

    window.exitonclick()

draw_art()
