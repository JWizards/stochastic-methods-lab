import matplotlib.pyplot as plt
import numpy as np


# rescale as per question
def rescale(Xs):
    return (Xs - np.mean(Xs))/np.std(Xs) 

N = 10000
binom_samples = np.sort(rescale(np.random.binomial(N, 0.5, N)))
normal = np.sort(rescale(np.random.normal(N, 0.5, N)))

plt.plot(normal, normal, label = 'normal distr.')
plt.plot(normal, binom_samples, label = 'binom distr.')

plt.title('QQplot for normal vs binomial')
plt.legend()
plt.show()

#Since N=10000 is large by the central limit theorem we have that binomial distribution is roughly normally distributed.
#This checks out on the graph as well
