import statistics
n=int(input())
s=[int(i) for i in input().split()]
s.sort()
print('%.2f'%statistics.mean(s))
print('%.2f'%statistics.median(s))
d=list(dict.fromkeys(s))
d.sort()
c=[]
p=[]
for i in range(len(d)):
    c.append(s.count(d[i]))
j=0
for i in c:
    if i==max(c):
        p.append(d[j])
    j=j+1
print(min(p))
print('%.2f'%statistics.stdev(s))
import numpy as np
import scipy.stats
a=np.array(s)
def ci(s,confidence=0.95):
    a=np.array(s)
    a=1.0*np.array(a)
    k=len(a)
    m,se=np.mean(a),scipy.stats.sem(a)
    h=se*scipy.stats.t.ppf((1+confidence)/2.,k-1)
    return m-h,m+h
print(ci(s))
