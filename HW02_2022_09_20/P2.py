#Abdullah Irfan Basheer HW2.2

from scipy.optimize import brentq



c = 0.1 # 10% 
n = 10 #10 years
m = 2 #semi annual

#relevant function
#Solve for me... SOLVE FOR ME!
f = lambda r : c/r + (1- c/r)/((1+r/m)**(n*m)) - 0.75 

print("IRR needed is ", brentq(f,-0.1,1))