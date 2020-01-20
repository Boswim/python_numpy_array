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
#data8 = np.genfromtxt('CSV/8.csv', delimiter=",", skip_header=True, usecols=(2,60))
#data9 = np.genfromtxt('CSV/9.csv', delimiter=",", skip_header=True, usecols=(2,60))
#data10 = np.genfromtxt('CSV/10.csv', delimiter=",", skip_header=True, usecols=(2,60))
#data11 = np.genfromtxt('CSV/11.csv', delimiter=",", skip_header=True, usecols=(2,60))
#data12 = np.genfromtxt('CSV/12.csv', delimiter=",", skip_header=True, usecols=(2,60))
#data13 = np.genfromtxt('CSV/13.csv', delimiter=",", skip_header=True, usecols=(2,60))
#data14 = np.genfromtxt('CSV/14.csv', delimiter=",", skip_header=True, usecols=(2,60))
#data15 = np.genfromtxt('CSV/15.csv', delimiter=",", skip_header=True, usecols=(2,60))
#data16 = np.genfromtxt('CSV/16.csv', delimiter=",", skip_header=True, usecols=(2,60))
#data17 = np.genfromtxt('CSV/17.csv', delimiter=",", skip_header=True, usecols=(2,60))
#data18 = np.genfromtxt('CSV/18.csv', delimiter=",", skip_header=True, usecols=(2,60))
#data19 = np.genfromtxt('CSV/19.csv', delimiter=",", skip_header=True, usecols=(2,60))
#data20 = np.genfromtxt('CSV/20.csv', delimiter=",", skip_header=True, usecols=(2,60))
#data21 = np.genfromtxt('CSV/21.csv', delimiter=",", skip_header=True, usecols=(2,60))
#data22 = np.genfromtxt('CSV/22.csv', delimiter=",", skip_header=True, usecols=(2,60))
#data23 = np.genfromtxt('CSV/23.csv', delimiter=",", skip_header=True, usecols=(2,60))
#data24 = np.genfromtxt('CSV/24.csv', delimiter=",", skip_header=True, usecols=(2,60))
#data25 = np.genfromtxt('CSV/25.csv', delimiter=",", skip_header=True, usecols=(2,60))
#data26 = np.genfromtxt('CSV/26.csv', delimiter=",", skip_header=True, usecols=(2,60))
#data27 = np.genfromtxt('CSV/27.csv', delimiter=",", skip_header=True, usecols=(2,60))
#data28 = np.genfromtxt('CSV/28.csv', delimiter=",", skip_header=True, usecols=(2,60))
#data29 = np.genfromtxt('CSV/29.csv', delimiter=",", skip_header=True, usecols=(2,60))
#data30 = np.genfromtxt('CSV/30.csv', delimiter=",", skip_header=True, usecols=(2,60))



# declare tube, used as a string in the export csv file
tube1=('tube_1')
tube2=('tube_2')
tube3=('tube_3')
tube4=('tube_4')
tube5=('tube_5')
tube6=('tube_6')
tube7=('tube_7')
#tube8=('tube_8')
#tube9=('tube_9')
#tube10=('tube_10')
#tube11=('tube_11')
#tube12=('tube_12')
#tube13=('tube_13')
#tube14=('tube_14')
#tube15=('tube_15')
#tube16=('tube_16')
#tube17=('tube_17')
#tube18=('tube_18')
#tube19=('tube_19')
#tube20=('tube_20')
#tube21=('tube_21')
#tube22=('tube_22')
#tube23=('tube_23')
#tube24=('tube_24')
#tube25=('tube_25')
#tube26=('tube_26')
#tube27=('tube_27')
#tube28=('tube_28')
#tube29=('tube_29')
#tube30=('tube_30')

# array from every csv-file, nan= ignore empty cells, min/max and average value from every csv-file
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
#p8=np.array(data8)
#min8=np.nanmin(p8)
#max8=np.nanmax(p8)
#gem8=np.nanmedian(p8)
#t8=tube8,min8, max8, gem8
#p9=np.array(data9)
#min9=np.nanmin(p9)
#max9=np.nanmax(p9)
#gem9=np.nanmedian(p9)
#t9=tube9,min9, max9, gem9
#p10=np.array(data10)
#min10=np.nanmin(p10)
#max10=np.nanmax(p10)
#gem10=np.nanmedian(p10)
#t10=tube10,min10, max10, gem10
#p11=np.array(data11)
#min11=np.nanmin(p11)
#max11=np.nanmax(p11)
#gem11=np.nanmedian(p11)
#t11=tube11,min11, max11, gem11
#p11=np.array(data11)
#min11=np.nanmin(p11)
#max11=np.nanmax(p11)
#gem11=np.nanmedian(p11)
#t11=tube11,min11, max11, gem11
#p12=np.array(data12)
#min12=np.nanmin(p12)
#max12=np.nanmax(p12)
#gem12=np.nanmedian(p12)
#t12=tube12,min12, max12, gem12
#p13=np.array(data13)
#min13=np.nanmin(p13)
#max13=np.nanmax(p13)
#gem13=np.nanmedian(p13)
#t13=tube13,min13, max13, gem13
#p14=np.array(data14)
#min14=np.nanmin(p14)
#max14=np.nanmax(p14)
#gem14=np.nanmedian(p14)
#t14=tube14,min14, max14, gem14
#p15=np.array(data15)
#min15=np.nanmin(p15)
#max15=np.nanmax(p15)
#gem15=np.nanmedian(p15)
#t15=tube15,min15, max15, gem15
#p16=np.array(data16)
#min16=np.nanmin(p16)
#max16=np.nanmax(p16)
#gem16=np.nanmedian(p16)
#t16=tube16,min16, max16, gem16
#p17=np.array(data17)
#min17=np.nanmin(p17)
#max17=np.nanmax(p17)
#gem17=np.nanmedian(p17)
#t17=tube17,min17, max17, gem17
#p18=np.array(data18)
#min18=np.nanmin(p18)
#max18=np.nanmax(p18)
#gem18=np.nanmedian(p18)
#t18=tube18,min18, max18, gem18
#p19=np.array(data19)
#min19=np.nanmin(p19)
#max19=np.nanmax(p19)
#gem19=np.nanmedian(p19)
#t19=tube19,min19, max19, gem19
#p20=np.array(data20)
#min20=np.nanmin(p20)
#max20=np.nanmax(p20)
#gem20=np.nanmedian(p20)
#t20=tube20,min20, max20, gem20
#p21=np.array(data21)
#min21=np.nanmin(p21)
#max21=np.nanmax(p21)
#gem21=np.nanmedian(p21)
#t21=tube21,min21, max21, gem21
#p22=np.array(data22)
#min22=np.nanmin(p22)
#max22=np.nanmax(p22)
#gem22=np.nanmedian(p22)
#t22=tube22,min22, max22, gem22
#p23=np.array(data23)
#min23=np.nanmin(p23)
#max23=np.nanmax(p23)
#gem23=np.nanmedian(p23)
#t23=tube23,min23, max23, gem23
#p24=np.array(data24)
#min24=np.nanmin(p24)
#max24=np.nanmax(p24)
#gem24=np.nanmedian(p24)
#t24=tube24,min24, max24, gem24
#p25=np.array(data25)
#min25=np.nanmin(p25)
#max25=np.nanmax(p25)
#gem25=np.nanmedian(p25)
#t25=tube25,min25, max25, gem25
#p26=np.array(data26)
#min26=np.nanmin(p26)
#max26=np.nanmax(p26)
#gem26=np.nanmedian(p26)
#t26=tube26,min26, max26, gem26
#p27=np.array(data27)
#min27=np.nanmin(p27)
#max27=np.nanmax(p27)
#gem27=np.nanmedian(p27)
#t27=tube27,min27, max27, gem27
#p28=np.array(data28)
#min28=np.nanmin(p28)
#max28=np.nanmax(p28)
#gem28=np.nanmedian(p28)
#t28=tube28,min28, max28, gem28
#p29=np.array(data29)
#min29=np.nanmin(p29)
#max29=np.nanmax(p29)
#gem29=np.nanmedian(p29)
#t29=tube29,min29, max29, gem29
#p30=np.array(data30)
#min30=np.nanmin(p30)
#max30=np.nanmax(p30)
#gem30=np.nanmedian(p30)
#t30=tube30,min30, max30, gem30

#arr now working till tube_7, rest has to be filled when everything will be activated
arr=np.array([t1,t2,t3,t4,t5,t6,t7])
#print statement can be deleted, is only for check
print(t1,t2,t3)
np.savetxt('my_result.csv',arr, delimiter=',', fmt= '%s', header='minimum, maximum, average', footer='testfile 3D Wearscan')








