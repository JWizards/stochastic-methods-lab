import numpy as np
import matplotlib.pyplot as plt

#generate a path
def gen_path(N):
    dw = np.random.normal(0,1,N)*np.sqrt(1/N)
    dw[0] = 0 #for convention's sake
    return np.cumsum(dw);

#setup
mu = 0.7
sigma = 0.4

#partition is number of intervals [0,1] is broken into
partition = 500
Xs = np.linspace(0, 1, partition)
#generate a thousand paths
paths = [np.exp((mu - 1/2*sigma*sigma)*Xs + sigma*gen_path(partition)) for i in range(1000)]

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
plt.title("Geometric Brownian Motion Paths")
plt.xlabel("Time")
plt.ylabel("Brownian Paths")
plt.legend()

plt.show()