import random
import turtle

# Module variables. Will be intialized in _initialize()
# A,B,C are the three vertices of the triangle we use.
A,B,C=None,None,None

# Length of each side.
L=None

# Our turtle
T = None

def _initialize():
 global A,B,C,L,T
 L = 500
 T = turtle.Turtle()
 T.shape('blank')
 T.speed(0)
 T.up()
 T.goto(-0.5*L, -0.43*L)
 T.down()
 A = T.pos()
 T.forward(L)
 B = T.pos()
 T.left(120)
 T.forward(L)
 C = T.pos()
 T.goto(A)

def random_inside_point():
 x = random.random()
 y = random.random()
 if x+y >= 1:
  x = 1-x
  y = 1-y
 b = B - A
 c = C - A
 return A + b*x + c*y

def next_point(p):
 global A,B,C,L,T
 v = random.choice([A,B,C])
 return (p+v)*0.5

def main():
  global A,B,C,L,T
  _initialize()
  for _ in xrange(10000):
   T.up()
   p = random_inside_point()
   for __ in xrange(5):
     p = next_point(p)
   T.goto(p)
   T.down()
   T.dot(1)

  turtle.exitonclick()
  turtle.mainloop()

main()
