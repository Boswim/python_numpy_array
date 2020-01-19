import os
import csv
import numpy as np
from numpy import genfromtxt

# used files sh11 in level A
data1 = np.genfromtxt('CSV/1.csv', delimiter=",", skip_header=True, usecols=(2,60))
data2 = np.genfromtxt('CSV/1.1.csv', delimiter=",", skip_header=True, usecols=(2,60))
data3 = np.genfromtxt('CSV/3.csv', delimiter=",", skip_header=True, usecols=(2,60))
data4 = np.genfromtxt('CSV/4.csv', delimiter=",", skip_header=True, usecols=(2,60))
data5 = np.genfromtxt('CSV/5.csv', delimiter=",", skip_header=True, usecols=(2,60))
data6 = np.genfromtxt('CSV/6.csv', delimiter=",", skip_header=True, usecols=(2,60))
data7 = np.genfromtxt('CSV/7.csv', delimiter=",", skip_header=True, usecols=(2,60))


tube1=('tube_1')
tube2=('tube_2')
tube3=('tube_3')
tube4=('tube_4')
tube5=('tube_5')
tube6=('tube_6')
tube7=('tube_7')

a=np.array(data1)
amin= np.nanmin(a)
amax= np.nanmax(a)
agem=np.nanmedian(a)
t1= tube1,amin,amax,agem
b=np.array(data2)
bmin= np.nanmin(b)
bmax= np.nanmax(b)
bgem=np.nanmedian(b)
t2=tube2,bmin,bmax,bgem
c=np.array(data3)
cmin= np.nanmin(c)
cmax= np.nanmax(c)
cgem=np.nanmedian(c)
t3=tube3,cmin,cmax,cgem
p4=np.array(data4)
min4=np.nanmin(p4)
max4=np.nanmax(p4)
gem4=np.nanmedian(p4)
t4=tube4,min4, max4, gem4
p5=np.array(data5)
min5=np.nanmin(p5)
max5=np.nanmax(p5)
gem5=np.nanmedian(p5)
t5=tube5,min5, max5, gem5
p6=np.array(data6)
min6=np.nanmin(p6)
max6=np.nanmax(p6)
gem6=np.nanmedian(p6)
t6=tube6,min6, max6, gem6
p7=np.array(data7)
min7=np.nanmin(p7)
max7=np.nanmax(p7)
gem7=np.nanmedian(p7)
t7=tube7,min7, max7, gem7
arr=np.array([t1,t2,t3,t4,t5,t6,t7])
print(t1,t2,t3)
np.savetxt('my_result.csv',arr, delimiter=',', fmt= '%s', header='minimum, maximum, average', footer='testfile 3D Wearscan')








