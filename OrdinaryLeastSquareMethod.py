import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
d=pd.read_html('https://github.com/akiwelekar/MLModels/blob/master/aimarks2017.csv')
df=d[0]
x=np.array(df['mse']).reshape(-1,1)
y=np.array(df['ese']).reshape(-1,1)
rm=LinearRegression()
rm.fit(x,y)
print(rm.coef_)
print(rm.intercept_)
