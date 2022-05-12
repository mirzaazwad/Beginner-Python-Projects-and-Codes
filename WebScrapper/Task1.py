#Task1
#Importing the required modules or libraries
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os

#Read the data.csv using pandas to create a dataframe
df=pd.read_csv(os.path.dirname(__file__)+"/"+"data.csv") 

#Plot using matplotlib.pyplot
plt.plot(df['X'],df['Y'],label='Y vs X for data')
plt.suptitle('Task: Plot Them All')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.savefig('Task1')
#A bell curve is obtained
#Testing dataframe contents
print(df)

