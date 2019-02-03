#!/usr/bin/env python
#AUTHOR  = Amzker [amzker@protonmail.com]
#project = Simple Matrix Calculator
import os
os.system("clear")
os.system("figlet Amzker")
print "Solution"
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
#Matrix value
Ma = a11*(a22*a33 - a23*a32) - a12*(a21*a33 - a23*a31) + a13*(a21*a32 - a22*a31)
#Calculation Part of parts
Aa11 = (a22*a33 - a23*a32)
Aa12 = -(a21*a33 - a23*a31)
Aa13 = (a21*a32 - a22*a31)
Aa21 = -(a21*a33 - a31*a23)
Aa22 = (a11*a33 - a31*a13)
Aa23 = -(a11*a32 - a31*a12)
Aa31 = (a12*a23 - a13*a22)
Aa32 = -(a11*a23 - a13*a21)
Aa33 = (a11*a22 - a21*a12)
#Formula
Ainx = 1
NN1 = Aa11 * Ainx
NN2 = Aa21 * Ainx
NN3 = Aa31 * Ainx
NN4 = Aa12 * Ainx
NN5 = Aa22 * Ainx
NN6 = Aa32 * Ainx
NN7 = Aa13 * Ainx
NN8 = Aa23 * Ainx
NN9 = Aa33 * Ainx
#OUTPUT
print 'Matrix Value'
print Ma
print
print 'a11'
print NN1
print
print 'a12'
print NN2
print
print 'a13'
print NN3
print
print 'a21'
print NN4
print
print 'a22'
print NN5
print
print 'a23'
print NN6

print 'a31'
print NN7

print 'a32'
print NN8

print 'a33'
print NN9
