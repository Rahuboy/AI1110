#code to find theoretical values of probabilities, and write data to an excel file.

from openpyxl import load_workbook
import pandas as pd
import numpy as np

#function to find probabilities
def prob(x,list):
    return list[x]/sum(list.values())

if __name__ == "__main__":

    wb = load_workbook("tables/raw_data.xlsx").active

#reading data
    for items in wb.iter_rows(min_row=1, max_row=1, values_only=True):
        pass

    for freq in wb.iter_rows(min_row=2, max_row=2, values_only=True):
        pass

    list = dict((x,y) for x,y in zip(items,freq))
        
#creating list of probabilities
    problist = np.array([prob(i,list) for i in range(10)])

#printing probability values
    for i in range(10):
        x=prob(i,list)
        print("probability of occurrence of {} is {}".format(i,x))

#writing to excel file    
    df = pd.DataFrame(problist)
    df = df.transpose()
    df.to_excel('tables/probabilities.xlsx', header=False, index=False)
    