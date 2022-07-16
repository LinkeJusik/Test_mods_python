from math import *
import math as mt

def Calculadora_ln(n,a):
    if n==1:
        return 0
    else:
        x=Calculadora_ln(n-1,a)
        #print(x,"es una aproximación")
        x=x-(((pow(mt.e,x)-a))/(pow(mt.e,x)))
        return x