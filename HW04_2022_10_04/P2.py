import numpy as np

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



print(binomial_tree(eu_call, K=0.7, S = 1, T = 1, sigma = 0.5, rp = 0.02, n = 1000))

#K=0.7 S = 1, T = 1, sigma = 0.5, rp = 0.02, n = 1000
        