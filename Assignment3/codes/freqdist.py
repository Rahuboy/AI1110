import numpy as np
import pandas as pd

#reading from excel
read = pd.read_excel(r'tables/raw_data.xlsx')
raw_data = np.array(read)

#automatically generating bins and class intervals
bin = [84+2*i for i in range(9)] 
class_intervals = ["{}-{}".format(bin[i],bin[i+1]) for i in range(8)]

#using inbuilt function for frequencies / class indices
hist = np.histogram(raw_data,bins=bin)
print(hist[0])

#writing to excel file
write = pd.DataFrame({"Relative Humidity":class_intervals,"Frequency":hist[0]})
write.to_excel('tables/frequency_distribution.xlsx',index=False)
