import turtle
turtle.title ("TITLE NOISES")
choice = input("what shape you want?: ")
def circle():
  for i in range(180):
    turtle.forward(2)
    turtle.left(2)
def triangle():
  for i in range(3):
    turtle.left(120)
    turtle.forward(100)
if choice == "circle":
  circle()
if choice == "triangle":
  triangle()