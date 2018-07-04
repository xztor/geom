"""Implements the chaos game.

The chaos game works like this. Take a triangle (in this case, equilateral).
Now pick a random point inside the traingle. Now pick a random vertex and move
the point halfway towards it. Pick a new random vertex and move the point again
halfway towards it. Continue this a few times.

Now pick a new random point and repeat the above process. Do this for a lot
of points and see where they all end up. What does the pattern look like?

"""

import random
import turtle

# Module variables. Will be intialized in _initialize()
# A,B,C are the three vertices of the triangle we use.
A,B,C=None,None,None

# Length of each side
L=500

# Number of points
N=10000

# Number of chaos iterations for each point. 
I=5

# Our turtle
T=None

# Thickness of each point plotted.
DOT_THICKNESS=2

def _initialize():
  global A,B,C,L,T
  turtle.title("Chaos Game")
  T = turtle.Turtle()
  T.shape('blank')
  T.speed(0)
  T.up()
  # This puts the center of the triangle near the origin.
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
  global A,B,C
  v = random.choice([A,B,C])
  return (p+v)*0.5

def main():
  global I,N,T,DOT_THICKNESS
  _initialize()
  for _ in xrange(N):
   T.up()
   p = random_inside_point()
   for __ in xrange(I):
     p = next_point(p)
   T.goto(p)
   T.down()
   T.dot(DOT_THICKNESS)
  turtle.exitonclick()

main()
