from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

def monte_sample(T, mu, sigma, K, S0 = 1):
    val = S0*np.exp( (mu - sigma*sigma/2)*T + sigma*np.sqrt(T)*np.random.normal(0, 1))
    return np.max(val - K, 0)

def monte_expectation(N):
    sum = 0
    for i in range(N):
        sum += monte_sample(T, r, sigma, K)
    return sum/N

#values
S = 1
K = 0.8
sigma = 0.7
T = 1
r = 0.3

#the slides... verbatim
x = (np.log(S/K) + (r + sigma*sigma/2)*T)/(sigma*np.sqrt(T))
C = S*norm.cdf(x) - K*np.exp(-r*T)*norm.cdf(x - sigma*np.sqrt(T)) #Black Scholes Current Price


Xs = [i for i in range(1,1001)]
monte_Y = [monte_expectation(i) for i in Xs]

m, c = np.polyfit(np.log(Xs), np.log(np.abs(monte_Y - C)), 1)


errs = np.abs(monte_Y - C)
plt.plot(np.log(Xs), np.log(errs))
plt.plot(np.log(Xs), np.log(Xs)*m + c)

print("Rate of convergence in a log plot is ", m)

