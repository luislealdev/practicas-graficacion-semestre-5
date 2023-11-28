import turtle as tt

# list for storing points
points = []

def clic(x, y):
    # add the item to the list
    points.append((x, y))

    # draw point at clicked position
    tt.penup()
    tt.goto(x, y)
    tt.dot(10, 'red')
    tt.pendown()

    # Connect points to lines
    tt.clear()  # clean up canvas to redraw lines
    for i in range(len(points) - 1):
        tt.penup()
        tt.goto(points[i])
        tt.pendown()
        tt.goto(points[i + 1])

# set up config
tt.bgcolor('black')
tt.color('white')
tt.pensize(5)
tt.speed(3)
tt.hideturtle()
tt.title('Points and Lines')

# set up click function  
tt.onscreenclick(clic)

# keep window open
tt.mainloop()
