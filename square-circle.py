import turtle

def draw_shapes():
  window = turtle.Screen()
  window.bgcolor("red")
  
  brad = turtle.Turtle()
  brad.shape("circle")
  brad.color("yellow")

  for i in range(1,37):
    draw_square(brad)
    brad.right(10)
    brad.speed(50)

  window.exitonclick()

def draw_square(asquare):
  for i in range(1, 5):
    asquare.backward(100)
    asquare.left(90)

draw_shapes()
