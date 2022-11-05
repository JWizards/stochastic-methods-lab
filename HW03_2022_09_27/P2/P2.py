#Abdullah Irfan Basheer
import matplotlib.pyplot as plt
import csv
import re

read = csv.reader(open('data.csv', 'r'))

#7th index contains time data!
data = [(row[7][3:], row[9], row[5]) for row in read if row[7].startswith("SR_")]

def decode(x):
    x = re.findall("[0-9]+[YM]", x) #cut up list
    ret = 0
    for timeItem in x:
        if timeItem[-1] == 'Y':
            ret += float(timeItem[0:-1])/1.0
        else:
            ret += float(timeItem[0:-1])/12.0
    return ret

data = [(decode(x), float(y), z) for (x, y, z) in data]
data.sort(key = lambda item: item[1])

X = [x for (x,y,z) in data if z=='G_N_A']
Y = [y for (x,y,z) in data if z=='G_N_A']
plt.scatter(X, Y, s = 0.5, label = "AAA")


X = [x for (x,y,z) in data if z=='G_N_C']
Y = [y for (x,y,z) in data if z=='G_N_C']
plt.scatter(X, Y, s = 0.5, label = "all")



plt.xlabel('Maturity in years')
plt.ylabel('Yield percentages')
plt.title('Yield Curve')
plt.legend()
plt.show()