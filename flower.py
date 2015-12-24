import turtle

def draw_art():
  window = turtle.Screen()
  window.bgcolor("red")
  
  brad = turtle.Turtle()
  brad.shape("circle")
  brad.color("yellow")

  for i in range(1,37):
    draw_square(brad)
    brad.right(60)
    brad.speed(50)

  brad.right(180)
  brad.forward(60)
  brad.left(90)
  brad.forward(400)

  window.exitonclick()

def draw_square(asquare):
  for i in range(1, 5):
    asquare.backward(150)
    asquare.left(130)

draw_art()
