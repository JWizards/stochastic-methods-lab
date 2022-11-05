# HW1:P4 Abdullah Irfan Basheer

from scipy.optimize import brentq
import numpy as np

#C is cashflow, C1 at end of year 1
#P is Real Price
def IRR( C, P ):
    return brentq(NPV, -0.1, 1, args = (C, P))
    
#Cash flow, net present value
def NPV( rate, C, P ):
    sum = 0
    for i in range(len(C)):
        sum += C[i]/((1+rate)**(1+i))
    return sum - P


#run the above
C = 120.0 * np.arange(42,52)
P = 50000.0
print("needed interest rate is ", IRR(C, P))