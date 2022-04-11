#ICSE 2017 Grade 10 5(b)
# Rahul Ramachandran (cs21btech11049)

# I will assume that the investment is 5400 Rs. and backtrack to get an income of 450 Rs.
# I will divide the income by the investment to find the yield percentage

# function for income
def income(nshares, divperc, worth):
    return nshares*divperc*worth

# function for yield percent
def yieldperc(income, cost, nshares):
    return income/(cost*nshares)*100

nshares = 90
divperc = 0.1
worth = 50
cost = 60
inc = income(nshares, divperc, worth)
yp = yieldperc(inc, cost, nshares)
print("income is",inc)
print("yield percent is",yp)