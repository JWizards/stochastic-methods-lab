import numpy as np
import timeit


# C array of cash inputs C[0] being C1
# r fractional interest rate, ex: 2% becomes 0.02

C = 120.0 * np.arange(500,1200) # use 120.0 for massive speed difference
r = 0.01
# HW1:P1 Abdullah Irfan Basheer
#Part 1 explicit loop
def explicitLoop( C, r ):
    S = 0
    for i in range(len(C)):
        S += C[i]/((1+r)**(i+1))
    return S

#Part 2 horners scheme
def hornersLoop( C, r ):
    n = len(C) #number of payments in cashflow
    S = C[n-1]
    for i in range(n-1):
        S = S/(1+r) + C[(n-1) - (i+1)]
    return S/(1+r)  #one more factor since last term is 0 w.r.t Horners

#Part 3 polyval function
def evalPolyval( C, r ):
    Cflip = np.append( np.flip(C), [0.0]) # Re-order & append 0 for scheme.
    return np.polyval(Cflip, 1/(1+r))

#Part 4 dot product of vectors
def dotProduct( C, r ):
    n = len(C)
    facs = (1/(1+r)) ** ((np.array(range(n)) + 1)) #factors; r**[1, 2, ..., 10]
    return np.dot(C, facs)

#Outputs

Oexp  = timeit.Timer('explicitLoop( C , r )', 'from __main__ import explicitLoop, C, r')
Ohorner  = timeit.Timer('hornersLoop( C , r )', 'from __main__ import hornersLoop, C, r')
Opoly  = timeit.Timer('evalPolyval( C , r )', 'from __main__ import evalPolyval, C, r')
Odot  = timeit.Timer('dotProduct( C , r )', 'from __main__ import dotProduct, C, r')

# printing all results 
print("Explicit Loop Eval: ", explicitLoop( C , r ), "time = ", Oexp.timeit(1000))
print("Horner's Loop Eval: ", hornersLoop( C , r ), "time = ", Ohorner.timeit(1000))
print("Polyval Eval: ", evalPolyval( C , r ), "time = ", Opoly.timeit(1000))
print("Dot Product Eval: ", dotProduct( C , r ), "time = ", Odot.timeit(1000))