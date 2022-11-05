#Abdullah Irfan Basheer
#Abdullah Irfan Basheer
import numpy as np
import matplotlib.pyplot as plt
sp_time = np.arange(30,110) #stock price over time assuming linear

#x is stock price, s is strike price
def E_call(x, s):
    return np.maximum(0, x-s)

#x is stock price, s is strike price
def E_put(x, s):
    return np.maximum(0, s-x)





Y_call = lambda k : E_call(sp_time, k)
Y_put = lambda k : E_put(sp_time, k)

Y_sol = Y_put(50) - Y_put(70) + Y_put(90) - Y_put(70)

plt.plot(sp_time, Y_sol, label = "solution")


plt.xlabel("Stock Prices (0-200)")
plt.ylabel("Profit")
plt.title("Calls/Puts Over Stock Prices")
plt.show()