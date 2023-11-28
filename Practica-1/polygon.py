import turtle as tt

tt.setup(650, 650, 300, 200)
tt.bgcolor('black')

tt.color('white')
tt.pensize(4)
tt.speed(1)
tt.title('Polygon Generator')

def draw_polygon():
    """
    Draws a polygon based on user input for the number of sides.
    
    This function prompts the user to enter the number of sides for the polygon.
    It then calculates the angle required to draw each side of the polygon based on the number of sides.
    Finally, it uses the turtle module to draw the polygon with the specified number of sides.
    """
    n = int(input('Type the number of sides of the polygon: \n'))

    a = 180 - ((180 * (n - 2)) / n)

    for s in range(n):
        tt.forward(100)
        tt.left(a)

    tt.exitonclick()

draw_polygon()
