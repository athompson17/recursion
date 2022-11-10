## Comment your code!

def get_compound_interest_balance(p,r,t):
    #formula for compound interest
    amount = p * (pow((1 + (r/100)),t))
    
#how compound interest is made
    
    CI = amount - p
    
    return CI
#what the variables are for
p=float(input("Enter Principal Amount: "))
r=float(input("Enter Rate of Interest: "))
t=float(input("Enter Time Period in years: "))

print("Compound interest is",get_compound_interest_balance(p,r,t))


