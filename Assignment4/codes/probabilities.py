#code to find theoretical values of probability, assuming uniform distribution
import numpy as np

# Sample size
N = 10000

counter = 0


# finding empirical value of probability, by counting frequency. 
# Uniform distribution assumed.
for i in range(N):
    x = np.random.choice([i for i in range(10)])
    if(x == 6):
        counter = counter+1

# printing empirical value
print("Experimental value of probability of occurrence of 6 is",counter/N)
