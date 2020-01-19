import os
import csv
import numpy as np
from numpy import genfromtxt

# used files sh11 in level A
data1 = np.genfromtxt('CSV/1.csv', delimiter=",", skip_header=True, usecols=(2,44))
data2 = np.genfromtxt('CSV/1.1.csv', delimiter=",", skip_header=True, usecols=(2,44))
data3 = np.genfromtxt('CSV/3.csv', delimiter=",", skip_header=True, usecols=(2,44))

tube1=('tube_1')
tube2=('tube_2')
tube3=('tube_3')

a=np.array(data1)
amin= np.nanmin(a)
amax= np.nanmax(a)
agem=np.nanmedian(a)
t1= amin,amax,agem
b=np.array(data2)
bmin= np.nanmin(b)
bmax= np.nanmax(b)
bgem=np.nanmedian(b)
t2=bmin,bmax,bgem
c=np.array(data3)
cmin= np.nanmin(c)
cmax= np.nanmax(c)
cgem=np.nanmedian(c)
t3=cmin,cmax,cgem
arr=np.array([t1,t2,t3])
print(t1,t2,t3)
np.savetxt('my_result.csv',arr, delimiter=',', fmt=['%.1f','%.1f','%.1f'], header='minimum, maximum, average', footer='testfile 3D Wearscan')








