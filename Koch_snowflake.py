import turtle
t = turtle.Turtle()
t.screen.setup(1000, 1000)
t.shape('turtle')
t.speed(0)
t.color('blue')
t.fillcolor('cyan')
t.pensize(2)
t.penup()
t.goto(-400, -225)
t.pendown()

def Ray(n, k):
    if n!=1:
        Ray(n-1, k)
    else:
        t.forward(260*((1/3)**(k-1)))
    t.left(60)
    if n!=1:
        Ray(n-1, k)
    else:
        t.forward(260*((1/3)**(k-1)))
    t.right(120)
    if n!=1:
        Ray(n-1, k)
    else:
        t.forward(260*((1/3)**(k-1)))
    t.left(60)
    if n!=1:
        Ray(n-1, k)
    else:
        t.forward(260*((1/3)**(k-1)))

n = 5 #Changeable
t.begin_fill()
t.left(60)
if n!=0:
    Ray(n, n)
else:
    t.forward(260*3)
t.right(120)
if n!=0:
    Ray(n, n)
else:
    t.forward(260*3)
t.right(120)
if n!=0:
    Ray(n, n)
else:
    t.forward(260*3)
t.end_fill()
t.screen.mainloop()
