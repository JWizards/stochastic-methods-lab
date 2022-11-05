from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

def eu_call(S, K, u, d, n):
    probs = np.array([(u**(i))*((d)**(n-i)) for i in range(n+1)])
    return np.maximum(S*probs - K, 0)

def binomial_tree(payoff, n, rp, sigma, S, K, T):
    
    r = rp*T/n  #interest rate of step
    u = np.exp(sigma*np.sqrt(T/n)) #probability of stock going up
    d = 1/u
    
    pu = (np.exp(r) -d)/(u-d)
    
    C = payoff(S, K, u, d, n) #getting array of payoffs!
                           #Ordered ascending for a call. 
                           #(largest index is stock going highest scenario)
    
    for i in range(n):
        C = np.exp(-r)*( pu*C[1:n+1-i] + (1-pu)*C[0:n-i])
    return C[0]


#values
S = 1
K = 1.2
sigma = 0.5
T = 1
r = 0.03

#the slides... verbatim
x = (np.log(S/K) + (r + sigma*sigma/2)*T)/(sigma*np.sqrt(T))
C = S*norm.cdf(x) - K*np.exp(-r*T)*norm.cdf(x - sigma*np.sqrt(T)) #Black Scholes Current Price

#calculate C with binom pricing
Ns = np.arange(1, 550)
binom_pricing = [binomial_tree(eu_call, n, r, sigma, S, K, T) for n in Ns]

#errors from black scholes
errs = np.abs(binom_pricing - C)

#find reference line
coef, intercept = np.polyfit( np.log10(Ns), np.log10(errs), 1)
ref_line = lambda x : np.power(10, (coef*x  + intercept))

#plot errs and ref line 
plt.loglog(Ns, errs, Ns, ref_line(np.log10(Ns)))

print("You obtain a downward trend the top of which is roughly a straight line,")
print("you could also think of it as a straight line with a range of slopes")
print("The error scales with power", coef)
print("i.e error scales approximately linearly with 1/n or inversely with n")