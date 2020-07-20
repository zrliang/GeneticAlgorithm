# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 20:17:59 2020

@author: user
"""

Processtime=[[80,0,60],[75,86,94],[25,0,96],[78,95,89],[45,78,0],
              [12,0,65],[55,99,87],[11,0,16],[0,16,45],[43,56,21]]

cM1=[]
M1=[3,6,7,10] #測試
M2=[4,5,9,10] 
M3=[1,2,3,8]

import random
OrderJobM1=[]
OrderJobM2=[]
OrderJobM3=[]
for x in range(len(M1)):
    OrderJobM1.append(random.random())
cM1 = list(zip(M1,OrderJobM1))  #兩個一維轉成一個二維
nM1=sorted(cM1,key=(lambda x:x[1]),reverse=True) #二維排序
#print(nM1)  #排序結果
for x in range(len(M2)):
    OrderJobM2.append(random.random())
cM2 = list(zip(M2,OrderJobM2))  #兩個一維轉成一個二維
nM2=sorted(cM2,key=(lambda x:x[1]),reverse=True) #二維排序
#print(nM2)  #排序結果

for x in range(len(M3)):
    OrderJobM3.append(random.random())
cM3 = list(zip(M3,OrderJobM3))  #兩個一維轉成一個二維
nM3=sorted(cM3,key=(lambda x:x[1]),reverse=True) #二維排序
#print(nM3)  #排序結果



###---------M1-------
# 工作順序
nnM1=[]
for a in range(len(nM1)):
   # print(nM1[a][0]) >> Job幾 
    nnM1.append(nM1[a][0])
#print(nnM1)

# 開始時間
M1t=0
M1StartAnswer=M1t
M1StartT=[]
M1StartT.append(M1t)
for b in range(len(nnM1)-1):
   # M1StartT.append(Processtime[nnM1[b]-1][0])
    M1StartAnswer+=Processtime[nnM1[b]-1][0]
    M1StartT.append(M1StartAnswer)
    
# 結束時間
M1EndAnswer=M1t
M1EndT=[]
for b in range(len(nnM1)):
   # M1StartT.append(Processtime[nnM1[b]-1][0])
    M1EndAnswer+=Processtime[nnM1[b]-1][0]
    M1EndT.append(M1EndAnswer)
# 合併
M1Answer = list(zip(nnM1,M1StartT,M1EndT))
print(M1Answer)


###---------M2-------
nnM2=[]
 # 工作順序
for a in range(len(nM2)):
   # print(nM1[a][0]) >> Job幾 
    nnM2.append(nM2[a][0])
#print(nnM1)

# 開始時間
M2t=0
M2StartAnswer=M2t
M2StartT=[]
M2StartT.append(M2t)
for b in range(len(nnM2)-1):
   # M1StartT.append(Processtime[nnM1[b]-1][0])
    M2StartAnswer+=Processtime[nnM2[b]-1][1]
    M2StartT.append(M2StartAnswer)
    
# 結束時間
M2EndAnswer=M2t
M2EndT=[]
for b in range(len(nnM2)):
   # M1StartT.append(Processtime[nnM1[b]-1][0])
    M2EndAnswer+=Processtime[nnM2[b]-1][1]
    M2EndT.append(M2EndAnswer)
# 合併
M2Answer = list(zip(nnM2,M2StartT,M2EndT))
print(M2Answer)   
    
###---------M3-------
nnM3=[]
 # 工作順序
for a in range(len(nM3)):
   # print(nM1[a][0]) >> Job幾 
    nnM3.append(nM3[a][0])
#print(nnM1)

# 開始時間
M3t=0
M3StartAnswer=M3t
M3StartT=[]
M3StartT.append(M3t)
for b in range(len(nnM3)-1):
   # M1StartT.append(Processtime[nnM1[b]-1][0])
    M3StartAnswer+=Processtime[nnM3[b]-1][2]
    M3StartT.append(M3StartAnswer)
    
# 結束時間
M3EndAnswer=M3t
M3EndT=[]
for b in range(len(nnM3)):
   # M1StartT.append(Processtime[nnM1[b]-1][0])
    M3EndAnswer+=Processtime[nnM3[b]-1][2]
    M3EndT.append(M3EndAnswer)
# 合併
M3Answer = list(zip(nnM3,M3StartT,M3EndT))
print(M3Answer)   


#比較Makespan
'''
if(M1TotalT>M2TotalT and M1TotalT>M3TotalT):
    print("M1"+" "+ str(M1TotalT))
elif(M2TotalT>M1TotalT and M2TotalT>M3TotalT):
    print("M2"+" "+ str(M2TotalT))
else:
    print("M3"+" "+ str(M3TotalT))
'''
'''
A=[10,7,8]
B=[0,8,10]
C=[80,100,130]

ABC= list(zip(A,B,C))
print(ABC)
'''