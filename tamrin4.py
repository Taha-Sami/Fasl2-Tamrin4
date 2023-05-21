import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
### Part1
df=pd.read_csv("project_data.csv")
df_y=df[["<CLOSE>"]]
df_x=df.drop(labels=["<CLOSE>"],axis=1)
moving_average=[]
moving=[]
#print(len(df_y))
#print(type(df_y.loc[0]),type(df_y.loc[1]),df_y.loc[0]+df_y.loc[1])
for i in range(len(df_y)-9+1):
	moving_average.append((df_y.loc[i]+df_y.loc[i+1]+df_y.loc[i+2]+df_y.loc[i+3]+df_y.loc[i+4]+df_y.loc[i+5]+df_y.loc[i+6]+df_y.loc[i+7]+df_y.loc[i+8])/9)
#print(len(df_y))
plt.plot(range(0,3406),df_y,label="Close")
plt.plot(range(0,3406-8),moving_average,label="moving 9 day")
plt.legend()
plt.show()

