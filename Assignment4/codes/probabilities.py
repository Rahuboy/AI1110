#code to find theoretical values of probabilities, and write data to an excel file.

import pandas as pd
import numpy as np

# function to find probabilities
def prob(x,dict1):
    return dict1[x]/sum(dict1.values())



#reading data

df = pd.read_excel("tables/raw_data.xlsx");

items = df["Digit"]
frequency = df["Frequency"]

#creating arrays
itemarray = [i for i in items]
freqarray = [i for i in frequency]

#creating dictionary and probability list
dict1 = dict((x,y) for x,y in zip(itemarray,freqarray))

problist = np.array([prob(i,dict1) for i in range(10)])

# Sample size
N = 10000

counter = 0


# finding empirical value of probability, by counting frequency
for i in range(N):
    x = np.random.choice([i for i in range(10)], p = problist)
    if(x == 6):
        counter = counter+1

# printing empirical value
print("Experimental value of probability of occurrence of 6 is",counter/N)
