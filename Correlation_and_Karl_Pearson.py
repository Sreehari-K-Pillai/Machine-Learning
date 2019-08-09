import numpy as np

import pandas as pd

x = [15,12,8,8,7,7,7,6,5,3]
y = [10,25,17,11,13,17,20,13,9,15]

x = pd.Series(x)
print(x)

y = pd.Series(y)
print(y)

r = x.cov(y) / (x.std() * y.std())
print("%.3f"%(r))
