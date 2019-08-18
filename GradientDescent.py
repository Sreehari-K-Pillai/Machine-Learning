import pandas as pd
import numpy as np
d=pd.read_html('https://github.com/akiwelekar/MLModels/blob/master/aimarks2017.csv')
df=d[0]
mse_marks=np.array(df['mse'])
ese_marks=np.array(df['ese'])
m= 0
c =0
l =0.00001
epochs =10000
n = float(len(mse_marks))
for i in range(epochs): 
    pred = m*mse_marks + c 
    D_m = (-2/n) * sum(mse_marks * (ese_marks - pred))  
    D_c = (-2/n) * sum(ese_marks - pred) 
    m = m - l * D_m  
    c = c - l * D_c     
print (m, c)
