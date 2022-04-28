import turtle

def draw_triangle(points, color, t):
    t.fillcolor(color)
    t.up()
    t.goto(points[0][0], points[0][1])
    t.down()
    t.begin_fill()
    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    t.goto(points[0][0], points[0][1])
    t.end_fill()
def get_mid(p1, p2):
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]

def sierpinski(points, degree, t):
    color_grade = ["green", "blue", "red", "yellow", "orange", "brown"]
    color = color_grade[degree]
    degree -= 1
    draw_triangle(points, color, t)
    if degree > 0:
        sierpinski([points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])], degree, t)
        sierpinski([points[1], get_mid(points[1], points[0]), get_mid(points[1], points[2])], degree, t)
        sierpinski([points[2], get_mid(points[2], points[0]), get_mid(points[2], points[1])], degree, t)


def main():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_points = [[-180, -150], [0, 150], [180, -150]]
    sierpinski(my_points, 5, my_turtle)
    my_win.exitonclick()

main()