import numpy as np
import matplotlib.pyplot as plt

#generate a path
def gen_path(N):
    dw = np.random.normal(0,1,N)*np.sqrt(1/N)
    dw[0] = 0 #for convention's sake
    return np.cumsum(dw);


#partition is number of intervals [0,1] is broken into
partition = 600
Xs = np.linspace(0, 1, partition)
paths = [gen_path(partition) for i in range(1000)] #generate a thousand paths

#compute mean and std column-wise :))
uber_mean = np.mean(paths, axis=0)
uber_std = np.std(paths, axis=0)

#print first 10 paths
for i in range(10):
    plt.plot(Xs, paths[i], color='orange', alpha= 0.25)

#print mean, then std both above and below
plt.plot(Xs, uber_mean, color = 'blue')
plt.plot(Xs, uber_std, color='black')
plt.plot(Xs, -uber_std, color='black')

#show plots
plt.title("Standard Brownian Motion Paths")
plt.xlabel("Time")
plt.ylabel("Brownian Paths")
plt.show()