#!/usr/bin/python
#
# Count the number of triangles in a geometrical figure composed of lines.
# Input data consists of all lines in the figure, including all intersection
# points. Each data line is a single line in the figure, and lists all
# intersection points on that line as a space separated list. The points can be
# any alphanumeric string.
#
# Example: Consider the following figure.
#
#  a--b--c
#  |\ | /|
#  | \|/ |
#  |  d  |
#  |   \ |
#  |    \|
#  e-----f
#
# This will be represented as:
#
# a b c
# a d f
# e f
# a e
# c f
# b d
# c d
#
# Put the data in a file (say puz.txt) and run the program as:
# python count_triangles.py puz.txt
# 
# For the above figure, it will print 6.
#
# Note: No validation is done to check whether
# the data represents a valid 2D geometric figure.

import sys

def CountTriangles(filename):
  f=open(filename, 'r')
  lines=[set(line.split()) for line in f]
  points=set().union(*lines)

  def GetSegments():
    # All line segments, i.e. pairs of points on same line.
    for l in lines:
      for x in l:
        for y in l:
          if x < y:
            yield set([x, y])

  def GetTriangles():
    # Consider all 3-tuple of points.
    for a in points:
      for b in points:
        for c in points:
          # Uniquify by ensuring the points are in alphabetical order.
          if a < b and b < c:
            t=set([a,b,c])
            # Check all three sides of the triangle exist.
            if (set([a,b]) in segments
               and set([a,c]) in segments
               and set([b,c]) in segments):
              # And they are not all on the same line.
              if not any(map(t.issubset, lines)):
                yield t

  segments = list(GetSegments())
  return sorted([sorted(list(t)) for t in GetTriangles()])

def main(argv):
  file = argv[1] if len(argv) >= 2 else 'puz.txt'
  triangles = CountTriangles(file)
  print len(triangles)

if __name__ == "__main__":
  main(sys.argv)
