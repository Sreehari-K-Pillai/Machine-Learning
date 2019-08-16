import pandas as pd
from urllib.request import urlopen
from io import StringIO
import csv
data=urlopen('https://s3.amazonaws.com/hr-testcases/399/assets/trainingdata.txt').read().decode('ascii','ignore')
datafile=StringIO(data)
csvReader=csv.reader(datafile)
a=[]
b=[]
for i in csvReader:
    a.append(i[0])
    b.append(i[1])
time_charged=[float(i) for i in a]
time_lasted=[float(i) for i in b]
x = pd.Series(time_charged)
y = pd.Series(time_lasted)
r = x.cov(y)/(x.std()*y.std())
beta1=(r*y.std())/x.std()
beta0=y.mean()-(beta1*x.mean())
m=float(input(""))
y=(beta1*m)+beta0
print("%d" %y)
