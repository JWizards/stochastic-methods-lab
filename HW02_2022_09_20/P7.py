#Abdullah Irfan Basheer
import matplotlib.pyplot as plt
import numpy as np

from scipy.optimize import brent
 
#initial values
F = 1                     #min r independent of F
c = 0.1
m = 1
n = 30
h = 10
C = F*c/m

#FV
def FV(r, h = h, F = F, C = C, m = 1):
    y = r/m
    
    sum = F/((1+y)**(n-h))
    for i in range(1, n+1):
        sum += C/((1 + y)**(i-h))
    
    return sum

#plot
xx = np.linspace(0, 1, 10000) # create the spaceing for the x axis
plt.plot(xx,FV(xx))

plt.xlabel('Yield')
plt.ylabel('Future Value')
plt.title('Future Value vs. yield')
plt.show()


minr = brent(FV, brack = (0,1))
#solving for minimum price
print("minimum price = ", minr)
print("minimum FV = ", FV(minr))