#Abdullah Irfan Basheer
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

def call(S, K, u, d, n):
    probs = np.array([(u**(i))*((d)**(n-i)) for i in range(n+1)])
    return np.maximum(S*probs - K, 0)

def put(S, K, u, d, n):
    probs = np.array([(u**(i))*((d)**(n-i)) for i in range(n+1)])
    return np.maximum(K - S*probs, 0)


def binomial_tree_american(payoff, n, rp, sigma, S, K, T):
    
    r = rp*T/n  #interest rate of step
    u = np.exp(sigma*np.sqrt(T/n)) #probability of stock going up
    d = 1/u
    
    pu = (np.exp(r) -d)/(u-d)
    
    C = payoff(S, K, u, d, n)  #getting array of payoffs!
                               #Ordered ascending for a call. 
                               #(largest index is stock going highest scenario            
    for i in range(n):
        C = np.maximum(np.exp(-r)*( pu*C[1:n+1-i] + (1-pu)*C[0:n-i]) , payoff(S, K, u, d, n-1-i))

    return C[0]


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


#American call or put options
print("printing american call or put option example outputs")
print(binomial_tree_american(call, K=0.7, S = 1, T = 1, sigma = 0.5, rp = 0.02, n = 1000))
print(binomial_tree_american(put  , K=0.7, S = 1, T = 1, sigma = 0.5, rp = 0.02, n = 1000))

def price_american_put(a, b, n):
    return [binomial_tree_american(put  , K=i, S = 1, T = 1, sigma = 0.5, rp = 0.02, n = 1000)
            for i in np.arange(a, b, (b-a)/n)]
    

def price_eu_put(a, b, n):
    return [binomial_tree(put  , K=i, S = 1, T = 1, sigma = 0.5, rp = 0.02, n = 1000)
            for i in np.arange(a, b, (b-a)/n)]


sp_time = np.linspace(0,2, 30) #strike price over time assuming linear
plt.plot(sp_time, price_american_put(0, 2, 30), label = "american")
plt.plot(sp_time, price_eu_put(0, 2, 30), label = "european")

print("From the graph it is clear american puts produce more value")
plt.xlabel("Strike Prices (0-2)")
plt.ylabel("Option Prices")
plt.title("American Vs European option prices over strike price")
plt.legend()
plt.show()
    