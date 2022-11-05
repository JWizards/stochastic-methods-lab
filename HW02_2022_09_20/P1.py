# HW2.1 Abdullah Irfan Basheer
import numpy as np
from scipy.optimize import brentq

import timeit


#bisection method
def bisect(a, b, f, e = 0.000001):
    if f(a)*f(b) > 0:
        print("Invalid Inputs")
        raise Exception("Function does not satisfy Bisection method")
        
    if a >= b:
    #swap algo
        a = a + b
        b = a - b
        a = a - b 
    
    while (b-a) > e:
        #return on immediate solve
        if abs(f((a+b)/2)) < e:
            return (a+b)/2
        
        #narrow search band
        if f((a+b)/2)*f(a) < 0:
            b = (a+b)/2
        else:
            a = (a+b)/2
    
    return (a+b)/2


#Newton Raphson Method
def NRsolv(x, f, df = None, e = 0.000001):
    #activate finite difference in times of need!! LETS GOOOOOOOOO! 
    if df == None:
        df = lambda x : (f(x+0.00000001) - f(x))/0.00000001
        
    def NR(x):
        return x - f(x)/df(x)
    
    xo = x #xo is x_old
    x = NR(x)
    while abs(x - xo) > e:
        xo = x
        x = NR(x)
    
    return x

#Secant Method
def Stsolv(x, xo, f, e = 0.00001):    
    def Sec(x, xo):
        return (x - f(x)*(x - xo)/(f(x) - f(xo)), x)
    
    while abs(x - xo) > e:
        x , xo = Sec(x, xo)
                
    return x




#Objective Functions!

#Cash flow, net present value
def NPV( rate, C, P ):
    sum = 0
    for i in range(len(C)):
        sum += C[i]/((1+rate)**(1+i))
    return sum - P

#derivative of NPV
def dNPV( rate, C, P ):
    sum = 0
    for i in range(len(C)):
        sum += -(1+i)*C[i]/((1+rate)**(2+i))
    return sum


#C is cashflow, C1 at end of year 1
#P is Real Price
#run the above
C = 120.0 * np.arange(10,310)
P = 15000.0

NPVflat = lambda x : NPV(x, C, P)
dNPVflat = lambda x : dNPV(x, C, P)

#Outputs

OBi  = timeit.Timer('bisect(0,1,NPVflat)', 'from __main__ import bisect, NPVflat')
ONewt  = timeit.Timer('NRsolv(0, NPVflat, dNPVflat)', 'from __main__ import NRsolv, NPVflat, dNPVflat')
OSecant  = timeit.Timer('Stsolv(0.05, 0, NPVflat)', 'from __main__ import Stsolv, NPVflat')
OBrent  = timeit.Timer('brentq(NPV, -0.1, 1, args = (C, P))', 'from __main__ import brentq, NPV, C, P')

# printing all results 
print("Bisect's Eval: ", bisect(0,1,NPVflat) , "time = ", OBi.timeit(1000))
print("Newton's Eval: ", NRsolv(0, NPVflat, dNPVflat), "time = ", ONewt.timeit(1000))
print("Secant's Eval: ", NRsolv(0, NPVflat), "time = ", OSecant.timeit(1000))
print("Brentq's Eval: ", brentq(NPV, -0.1, 1, args = (C, P)) , "time = ", OBrent.timeit(1000))









