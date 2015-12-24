import turtle

def draw_shapes():
  window = turtle.Screen()
  window.bgcolor("red")

  draw_square()
  draw_circle()
  draw_triangle()

  window.exitonclick()

def draw_square():
  brad = turtle.Turtle()
  brad.shape("circle")
  brad.color("yellow")

  for i in range(1, 5):
    brad.backward(100)
    brad.left(90)

def draw_circle():
  angie = turtle.Turtle()
  angie.shape("square")
  angie.color("blue")
  angie.circle(100)

def draw_triangle():
  troy = turtle.Turtle()
  troy.shape("turtle")
  troy.color("grey")

  for i in range(1,4):
    troy.forward(200)
    troy.right(120)

draw_shapes()
