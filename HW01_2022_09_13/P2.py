# HW1:P2 Abdullah Irfan Basheer
# 2% monthly translates to 1/6 % monthly

#Observe we need ((((x - 2000)r -2000)r - 2000)r ...) = 0
# therefore x = 2000*SUM / r^360
# where r was (1 + r) but denoted as r simply for clarity

#Amount needed in bank to last exactly 30 years or 360 months
def amtNeed(wthdrw, rate, periods):
    sum = 0
    for i in range(periods):
        sum += (1+rate)**i
    sum *= wthdrw/((1+rate)**(periods-1))
    return sum

print("Amount needed at retirement is: ", amtNeed(2000, 0.02/12, 360))
need = amtNeed(2000, 0.02/12, 360)


#Here see that
# FV = A*(geometric sum of (1+r))

#Amount you need to deposit to obtain the above
def depositAmt(need, rate, periods):
    sum = 0
    for i in range(1, periods+1): #shifting since deposit at beginning of month
        sum += (1+rate)**i
    return need/sum

print("Amount to deposit monthly is: ", depositAmt(need, 0.02/12, 480))