#Abdullah Irfan Basheer
import matplotlib.pyplot as plt
import numpy as np


#Parameters
F = 100
m = 2
r = 0.08
n = 15 #FV in 15 years denoted as n

#assuming zero token bond since not specified in question
#t varies
def FV(t, rn, r = r, m = m, n = n, F = F):
    return F*((1+(rn/m))**(n*m))/((1 + (r/m))**(t*m))

#Plots
F1 = lambda n : FV(n, 0.06)
F2 = lambda n : FV(n, r)
F3 = lambda n : FV(n, 0.10)

xx = np.linspace(1, 30,  10000) # create the spaceing for the x axis

plt.plot(xx,F1(xx), label = "r = 0.06")
plt.plot(xx,F2(xx), label = "r = 0.08")
plt.plot(xx,F3(xx), label = "r = 0.10")

plt.xlabel('Time to maturity (in years)')
plt.ylabel('Forward Value')
plt.title('Price vs. Time to maturity')
plt.legend()
plt.show()

