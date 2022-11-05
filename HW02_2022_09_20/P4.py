import matplotlib.pyplot as plt
import numpy as np

#variables
F = 1000
n = 10

# Price for n and c function
def P(r, c, F = F, n = n):    
    return F*(c/r + (1 - c/r)/((1 + r)**n))

P1 = lambda r : P(r, 0.08)

xx = np.linspace(0, 1, 10000) # create the spaceing for the x axis


plt.plot(xx,P1(xx))

plt.xlabel('Yield')
plt.ylabel('Bond Price')
plt.title('Bond Price vs. Yield')
plt.show()


