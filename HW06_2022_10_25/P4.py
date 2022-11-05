import numpy as np
import matplotlib.pyplot as plt

#generate a path
def gen_path(N):
    dw = np.random.normal(0,1,N)*np.sqrt(1/N)
    dw[0] = 0 #for convention's sake
    return np.cumsum(dw);

T = 1
N = 1000

#by ito and Stratonovich denoted as ito and sto
#generate a path, with sufficient to points to enable sampling for ito and sto
W = gen_path(2*N + 2)

#compute ito and sto differences
ito_del = [W[i]*(W[i+2] - W[i]) for i in range(0,2*N, 2)]
sto_del = [W[i+1]*(W[i+2] - W[i]) for i in range(0,2*N, 2)]

#running sum/integral approx
sum_ito = np.cumsum(ito_del)
sum_sto = np.cumsum(sto_del)


Xs = np.linspace(0, 1, N)
plt.plot(Xs, sum_ito, label = 'Ito\'s Integral', color = 'orange', alpha = 0.75)
plt.plot(Xs, sum_sto, label = 'Stratovanich\'s Integral', color = 'blue', alpha = 0.75 )
plt.plot(Xs, W[0:2*N:2], label = 'Brownian Path', color = 'dimgrey')    #adjusting needed to fit with Xs

plt.title("Integral Comparisons")
plt.xlabel("Time")
plt.ylabel("Integral/Brownian Path")
plt.legend()

plt.show()

"""
Clearly Stratovanich's integral is always above Ito's Integral
"""


