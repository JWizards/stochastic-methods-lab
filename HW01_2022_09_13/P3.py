# HW1:P3 Abdullah Irfan Basheer
#r nominal yearly interest, P loan amount, m compounding periods, n years
def amortSchedule(r, P, m, n):
    
    
    amt = P*r/(m*(1 - (1 + r/m)**((-n)*m))) #amount to be paid every period
    
    reff = (1 + r/m)**m - 1
    
    print("Amount to be paid every period: ", amt)
    print("Effective interest rate: ", reff)
    print("-----------------------------------------------------------------------")
    
    data = [] #simulate table and store data
    #simulation style!
    for i in range(m*n):
        Pi = P*(1+r/m) #compound interest
        #month, amt paid, interest, principal paid, outstanding balance
        data.append([i+1, amt, min(Pi - P, amt), max(P - (Pi - amt), 0), Pi -amt])
        P = Pi - amt

    
        
    print("{:<8} {:<12} {:<12} {:<14} {:<20}".format( 'Month',
                                                'Amount Paid',
                                                'Interest',
                                                'Principal Paid',
                                                'Outstanding Balance')
           )
    
    print("{:_<8} {:_<12} {:_<12} {:_<14} {:_<20}".format('','','','',''))
    
    for v in data:
        mo, am, intr, pp, oba = v
        print ("{:<8} {:<12.8} {:<12.8} {:<14.8f} {:<20.8}".format( mo, am, intr, pp, oba))
    
    


amortSchedule(0.02, 500000, 12, 20)
    