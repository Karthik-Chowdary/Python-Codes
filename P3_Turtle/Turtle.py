import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(60)
    num_times = 0
    while(num_times<100):
        num = 0
        while(num<4):
            brad.forward(100)
            brad.right(90)
            num += 1
        brad.right(5)
        num_times += 1
    window.exitonclick()
draw_square()
    
