import turtle
import tkinter as TK

window = turtle.Screen()
window.bgcolor("#252525")
window.title("Hello Test!")
draw = turtle.Pen()
draw.speed(25)

sides = 25#int(input("Input how many sides to draw: "))
sideLength =100-190*(sides*.01)
angle = 360/sides
inangle = (180-angle)/(sides-2)
draw.setheading(90)
draw.up()
draw.setposition(sideLength*-2, sideLength*.5)
draw.down()

for i in range(sides):
    draw.color("cyan")
    draw.right(angle)
    draw.forward(sideLength)
    vertexPos = draw.pos()
    if(i<sides-2):
        vertexAngle=draw.heading()
        length = 1
        for x in range(i+1):
            if (x < sides-3):
                draw.setheading(vertexAngle)
                draw.color("lime")
                draw.left(inangle*(x+1))
                if(sides%2==1):
                    #draw.backward(sideLength*sides/3)
                    draw.backward(pow(sideLength,2)/(sides*.25))
                    draw.setposition(vertexPos)
                elif(x!=round(sides/2)-2):
                    draw.backward(pow(sideLength,2)/(sides*.25))
                    draw.setposition(vertexPos)
        #Draw shape contour
        draw.setheading(90)
        draw.right(angle*(i+1))

#for i in range(sides)

#colors=["blue","lime", "red", "cyan", "orange", "yellow"]

#for i in range(360):
    #draw.pencolor(colors[i%6])
    #draw.forward(350)
    #draw.left(124)
    #draw.circle(125)

TK.mainloop()
