import matplotlib.pyplot as plt
import numpy as np

#variables
F = 1000
r = 0.06
m = 2
 
# Price for n and c function
def P(n, c, F = F, r = r, m = m):    
    return F*(c/r + (1 - c/r)/((1 + r/m)**(n*m)))

def dP(n, c, F = F, r = r, m = m, e = 0.0000001):
    return (P(n,c,F,r+e, m) - P(n, c, F, r, m))/e 

#utilizing definition as per Lecture Note 6 where,
#volatility is differentiated w.r.t r and not y = (r/m) as would be in the book. 


dP1 = lambda n : -dP(n, 0.02)/P(n, 0.02)
dP2 = lambda n : -dP(n, 0.06)/P(n, 0.06)
dP3 = lambda n : -dP(n, 0.12)/P(n, 0.12)

xx = np.linspace(0, 100, 10000) # create the spaceing for the x axis

plt.plot(xx,dP1(xx), label = "r = 0.02")
plt.plot(xx,dP2(xx), label = "r = 0.06")
plt.plot(xx,dP3(xx), label = "r = 0.12")


plt.xlabel('Time to Maturity')
plt.ylabel('Price Volatility')
plt.title('Price Volatility vs. Time to maturity')
plt.legend()
plt.show()


