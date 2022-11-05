from scipy import special
import numpy as np
import matplotlib.pyplot as plt

#jth term out of n with prob p
def bin_term(j, n, p):
    return special.binom(n, j)*(p**j)*((1-p)**(n-j))

def plot_nbinom(n, p):
    q = 1 - p
    Xs = [(j - n*p)/np.sqrt(n*p*q) for j in range(0, n+1)]
    Ys = [np.sqrt(n*p*q)*bin_term(j, n, p) for j in range(n+1)]
    return (Xs, Ys)

def plot_gaussian(n, interv = 5):
    Xs = np.linspace(-interv, interv, n)
    Ys = [np.exp((-x)*x/2)/np.sqrt(2*np.pi) for x in Xs]
    return (Xs, Ys)

fig, ax = plt.subplots(1,2)

G_X, G_Y = plot_gaussian(1000)

X1, Y1 = plot_nbinom(10, 0.5)
X2, Y2 = plot_nbinom(100, 0.5)
ax[0].plot(G_X, G_Y, linewidth = 1, color = 'orange', label = 'gaussian')
ax[0].scatter(X1, Y1, color = 'green', label = 'n = 10, p = 0.5')
ax[0].scatter(X2, Y2, color = 'blue', label = 'n = 100, p = 0.5')
ax[0].set_xlim(-5, 5)
ax[0].legend()

X1, Y1 = plot_nbinom(10, 0.2)
X2, Y2 = plot_nbinom(100, 0.2)
ax[1].plot(G_X, G_Y, color = 'orange', label = 'gaussian')
ax[1].scatter(X1, Y1, color = 'green', label = 'n = 10, p = 0.2')
ax[1].scatter(X2, Y2, color = 'blue', label = 'n = 100, p = 0.2')
ax[1].set_xlim(-5, 5)
ax[1].legend()
plt.show()

#for large n the binom sample better approximates the gaussian distribution
#same for p closer to 0.5
