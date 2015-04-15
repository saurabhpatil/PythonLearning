import turtle

def triangle(size,t):
    t.speed(10)
    t.color("blue","green")
    t.shape("turtle")
    t.begin_fill()
    for i in range(1,4):
        t.forward(size)
        t.left(120)
    t.end_fill()


def recur(size,order,t):
    if order ==0:
        triangle(size,t)
    else:
        recur(size/2,order-1,t)
        t.forward(size)
        t.left(120)
        recur(size/2,order-1,t)
        t.forward(size)
        t.left(120)
        recur(size/2,order-1,t)
        t.forward(size)
        t.left(120)

saurabh=turtle.Turtle()
recur(300,5,saurabh)
