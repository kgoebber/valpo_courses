#!/bin/python

import sys
import numpy as np

c = 0
data = np.zeros((100,2))
#n = int(sys.argv[1])
for n in range(1,101):
 a = n
 b = 0

 while (a != 1.0):
  if (a % 2 == 0):
   a = a /2.
  else:
   a = 3*a + 1
  b = b + 1
#	print a
 print(n," is a wonderous number!")
 print("Total number of iterations ",+b)
 data[c,0]=n
 data[c,1]=b
 c = c + 1
filename="bloop.out"
np.savetxt(filename,data,fmt="%s")
