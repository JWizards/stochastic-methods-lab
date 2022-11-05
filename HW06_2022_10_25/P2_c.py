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

#generate a path
def gen_path(N):
    dw = np.random.normal(0,1,N)*np.sqrt(1/N)
    dw[0] = 0 #for convention's sake
    return np.cumsum(dw);


#setup
mu = 0.7
sigma = 0.4

#-------------------------------------------


#partition is number of intervals [0,1] is broken into
partition = 500
Xs_a = np.linspace(0, 1, partition)
#generate a thousand paths
paths_a = [np.exp((mu - 1/2*sigma*sigma)*Xs_a + sigma*gen_path(partition)) for i in range(1000)]

#compute mean and std column-wise :))
uber_mean_a = np.mean(paths_a, axis=0)
uber_std_a = np.std(paths_a, axis=0)

#---------now doing b

#partition is number of intervals [0,1] is broken into
partition = 600
Xs_b = np.linspace(0, 1, partition)
#generate a thousand paths
paths_b = [ gen_path_binom(partition, mu, sigma, 1) for i in np.arange(0,1000)]

#compute mean and std column-wise :))
uber_mean_b = np.mean(paths_b, axis=0)
uber_std_b = np.std(paths_b, axis=0)



#--------------------------------------------


plt.subplot(1,2,1)
#print first 10 paths
for i in range(6):
    plt.plot(Xs_a, paths_a[i], color='orange', alpha= 0.25)

#print mean, then std both above and below
plt.plot(Xs_a, uber_mean_a, color = 'blue', label = 'mean')
plt.plot(Xs_a, uber_mean_a + uber_std_a, color='black', label = 'std')
plt.plot(Xs_a, uber_mean_a - uber_std_a, color='black')

#show plots
plt.title("Geometric Brownian Motion Paths")
plt.xlabel("Time")
plt.ylabel("Brownian Paths")
plt.legend()

plt.subplot(1,2,2)
#print first 10 paths
for i in range(6):
    plt.plot(Xs_b, paths_b[i], color='orange', alpha= 0.25)

#print mean, then std both above and below
plt.plot(Xs_b, uber_mean_b, color = 'blue', label = 'mean')
plt.plot(Xs_b, uber_mean_b + uber_std_b, color='black', label = 'std')
plt.plot(Xs_b, uber_mean_b - uber_std_b, color='black')

#show plots
plt.title("Calibrated Binomial Tree Paths")
plt.xlabel("Time")
plt.ylabel("Binomial paths")
plt.legend()

plt.show()
#Clearly the graphs look very similar and the methods approximate one and another
   

