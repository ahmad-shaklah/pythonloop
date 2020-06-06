import turtle

def draw(square):

    for i in range(4) :
        square.forward(150)
        square.right(90)

def move():

    window = turtle.Screen()
    window.bgcolor("#ffffff")

    creature = turtle.Turtle()
    creature.shape('turtle')
    creature.color('black')
    creature.pensize(4)
    creature.speed(1000)
    creature.shapesize(1)
    
    for i in range(20) :


        draw(creature)
        creature.right(20)
    turtle.color('blue')
    style = ('Courier', 50, 'italic')
    turtle.write('created by ahmad shaklah <0>_<*>', font=style, align='center')

    window.mainloop()

move()
