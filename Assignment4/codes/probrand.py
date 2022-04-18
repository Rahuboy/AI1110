#Code to show that theoretical values match experimental values using randomization

import numpy as np
import pandas as pd

#Sample size
N = 2500

counter = 0

#reading from excel
read = pd.read_excel(r'tables/probabilities.xlsx')
data = np.array(read)
problist = [i for i in data[0]]

#finding empirical value of probability, by counting frequency
for i in range(N):
    x = np.random.choice([i for i in range(10)], p = problist)
    if(x == 6):
        counter = counter+1

print("Experimental value of probability is",counter/N)
print("Theoretical value is 0.07")