import numpy as np

# For a given trial, returns the index of the first complement of the first toss
# If the complement doesn't occur in the array, then returns the max number of tosses in the trial (t) 
def findnumber(x,t):
    if(x[0]==0):
        y=x.tolist().index(1)
        if y>0:
            return y
        else:
            return t
    else:
        y=x.tolist().index(0)
        if y>0:
            return y
        else:
            return t



#Total number of trials
N = 10000

#parameters
p=1/3
q=1-p
t=40 #maximum number of tosses in a trial

#generates N binary t-tuples
probarr = np.random.choice([1,0],size=(N,t), p=[p,q])

#uses the in-built function map on the iterable probarr
mapped = map(lambda x: findnumber(x,t), probarr)
finarr = list(mapped)

print(sum(finarr)/N) #empirical probability
print(p/q+q/p) #theoretical probability
