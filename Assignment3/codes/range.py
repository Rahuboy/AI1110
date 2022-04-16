import numpy as np
import pandas as pd

#reading from excel
read = pd.read_excel(r'tables/raw_data.xlsx')
raw_data = np.array(read)

max = np.amax(raw_data)
min = np.amin(raw_data)

print("Maximum value of humidity is",max)
print("Minimum value of humidity is",min)
print("The range of the data is therefore {} - {} = {}".format(max,min,max-min))