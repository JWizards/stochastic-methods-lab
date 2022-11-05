import numpy as np
import matplotlib.pyplot as plt

#generate a path
def gen_path_binom(N, rp, sigma, T):
    r = rp*T/N  #interest rate of step
    u = np.exp(sigma*np.sqrt(T/N)) #probability of stock going up
    d = 1/u
    
    pu = (np.exp(r) -d)/(u-d)

    
    dw = np.random.choice([u, d], size=N, p=[pu, 1 - pu])
    dw[0] = 1 
    
    return np.cumprod(dw);

#setup
mu = 0.7
sigma = 0.4

#partition is number of intervals [0,1] is broken into
partition = 600
Xs = np.linspace(0, 1, partition)
#generate a thousand paths
paths = [ gen_path_binom(partition, mu, sigma, 1) for i in np.arange(0,1000)]

#compute mean and std column-wise :))
uber_mean = np.mean(paths, axis=0)
uber_std = np.std(paths, axis=0)


#print first 10 paths
for i in range(6):
    plt.plot(Xs, paths[i], color='orange', alpha= 0.25)

#print mean, then std both above and below
plt.plot(Xs, uber_mean, color = 'blue', label = 'mean')
plt.plot(Xs, uber_mean + uber_std, color='black', label = 'std')
plt.plot(Xs, uber_mean - uber_std, color='black')

#show plots
plt.title("Calibrated Binomial Tree Paths")
plt.xlabel("Time")
plt.ylabel("Brownian Paths")
plt.legend()

plt.show()