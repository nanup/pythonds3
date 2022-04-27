import turtle
import random

def tree(branch_len, t):
    angle = random.randrange(15, 46)
    num = random.randrange(10, 16)
    if branch_len > 5:
        t.width(branch_len // 4)
        if branch_len < 30:
            t.color("green")
        else:
            t.color("brown")
        t.forward(branch_len)
        t.right(angle)
        tree(branch_len - num, t)
        t.left(2 * angle)
        tree(branch_len - num, t)
        if branch_len < 30:
            t.color("green")
        else:
            t.color("brown")
        t.right(angle)
        t.backward(branch_len)


def main():
    t = turtle.Turtle()
    win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(75, t)
    win.exitonclick()

main()
