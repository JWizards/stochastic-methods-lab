#Abdullah Irfan Basheer
import numpy as np
import matplotlib.pyplot as plt
sp_time = np.arange(0,200) #stock price over time assuming linear

#x is stock price, s is strike price
def E_call(x, s):
    return np.maximum(0, x-s)

#x is stock price, s is strike price
def E_put(x, s):
    return np.maximum(0, s-x)

plt.plot(sp_time, E_call(sp_time, 100), label = "call")
plt.plot(sp_time, E_put(sp_time, 100), label = "put")

plt.xlabel("Stock Prices (0-200)")
plt.ylabel("Profit")
plt.title("Calls/Puts Over Stock Prices")
plt.legend()
plt.show()
    


