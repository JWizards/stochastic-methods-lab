from scipy import special
import numpy as np
import matplotlib.pyplot as plt


#stirlings approximation for factorials
stirlings = lambda n : np.sqrt(2*np.pi*n)*np.power(n/np.exp(1), n)


#calculation of values to plot
Ns = np.arange(1,101)
err = np.absolute((special.factorial(Ns) - stirlings(Ns))/stirlings(Ns))


#plot of things
plt.loglog(Ns, err)
plt.title("errors going down")
plt.xlabel("Ns going from 1 to 100")
plt.ylabel("error vals")


#The plot's rough slope
slope, intercept = np.polyfit(np.log(Ns), np.log(err), 1)
print("The slope is ", slope)

#Since the slope is roughly -1 on the logscale the error is proportional to 1/n
# therefore the next order term must be O(1/n)