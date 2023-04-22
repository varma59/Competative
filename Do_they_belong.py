Do They Belong?

10

11

12

13

ALL

14

A triangle formed by the three points alx1, y1), b(x2, y2) and c(x3, y3) is a non- degenerate triangle if the following rules are respected (/ab/ is the length of the line between points a and b):

15

16

Θ

17

18

19

Jab]+|bc|> [ac]

|bc|+|ac|> [ab]

[ab]+[ac]> [be]

20

21

22

23

A point belongs to a triangle if it lies

somewhere on or inside the triangle. Given

two points p = (xp, yp) and q = (xq, yq), return

the correct scenario number:

24

25 26

3

27

28

d

29

30

31 >

⚫0. If the triangle abc does not form a valid non-degenerate triangle.

1: If point p belongs to the triangle but point q does not. 2. If point q belongs to the triangle but point

p does not. • 3 If both points p and q belong to the

triangle.

⚫ 4 If neither point p nor point q belong to the

triangle.



Program: 
  
#!/bin/python3

import math
import os
import random
import re
import sys




def pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
    if(isTriangleValid(x1, y1, x2, y2, x3, y3,) == False):
        return '0'
    elif(isInside(x1, y1, x2, y2, x3, y3, xp, yp) == True and isInside(x1, y1, x2, y2, x3, y3, xq, yq) == False):
        return '1'
    elif(isInside(x1, y1, x2, y2, x3, y3, xp, yp) == False and isInside(x1, y1, x2, y2, x3, y3, xq, yq) == True):
        return '2'
    elif(isInside(x1, y1, x2, y2, x3, y3, xp, yp) == True and isInside(x1, y1, x2, y2, x3, y3, xq, yq) == True):
        return '3'
    elif(isInside(x1, y1, x2, y2, x3, y3, xp, yp) == False and isInside(x1, y1, x2, y2, x3, y3, xq, yq) == False):
        return '4'
    
def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * ( y1 - y2)) / 2.0)
    
def isTriangleValid(x1, y1, x2, y2, x3, y3):
    A = (
        x1 * (y2 - y3) +
        x2 * (y3 - y1) +
        x3 * (y1 - y2)
    )
    if A == 0:
        return False
    else:
        return True
    
def isInside(x1, y1, x2, y2, x3, y3, x, y):
    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(x, y, x2, y2, x3, y3)
    A2 = area(x1, y1, x, y, x3, y3)
    A3 = area(x1, y1, x2, y2, x, y)
        
    if(A == A1 + A2 + A3):
         return True
    else:
        return False

if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1 = int(input().strip())

    y1 = int(input().strip())

    x2 = int(input().strip())

    y2 = int(input().strip())

    x3 = int(input().strip())

    y3 = int(input().strip())

    xp = int(input().strip())

    yp = int(input().strip())

    xq = int(input().strip())

    yq = int(input().strip())

    result = pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq)

    fptr.write(str(result) + '\n')

    fptr.close()
