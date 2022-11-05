import matplotlib.pyplot as plt
import numpy as np

#variables
F = 1000
r = 0.06

# Price for n and c function
def P(n, c, F = F, r = r):    
    return F*(c/r + (1 - c/r)/((1 + r)**n))

P1 = lambda n : P(n, 0.02)
P2 = lambda n : P(n, 0.06)
P3 = lambda n : P(n, 0.12)

xx = np.linspace(0, 100, 10000) # create the spaceing for the x axis

plt.plot(xx,P1(xx), label = "r = 0.02")
plt.plot(xx,P2(xx), label = "r = 0.06")
plt.plot(xx,P3(xx), label = "r = 0.12")

plt.xlabel('Time to Maturity')
plt.ylabel('Price')
plt.title('Price vs. Time to maturity')
plt.legend()
plt.show()


