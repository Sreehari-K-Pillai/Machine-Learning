import pandas as pd
physics_score = [15,12,8,8,7,7,7,6,5,3]
history_score = [10,25,17,11,13,17,20,13,9,15]
x = pd.Series(physics_score)
y = pd.Series(history_score)
r = x.cov(y)/(x.std()*y.std())
beta1=(r*y.std())/x.std()
beta0=y.mean()-(beta1*x.mean())
m=int(input(""))
y=(beta1*m)+beta0
print("%.1f" %y)
