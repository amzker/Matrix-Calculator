#!/usr/bin/env python
#AUTHOR  = Amzker [amzker@protonmail.com]
#project = Simple Matrix Calculator
import os
os.system("clear")
print "Here is Your Value of Matrix"
#value part
a11 = 1
a12 = 2
a13 = 3
a21 = 2
a22 = 3
a23 = 1
a31 = 3
a32 = 1
a33 = 2
#Formula
Ma = a11*(a22*a33 - a23*a32) - a12*(a21*a33 - a23*a31) + a13*(a21*a32 - a22*a31)
#output
print Ma

