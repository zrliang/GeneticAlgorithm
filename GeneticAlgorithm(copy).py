# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 19:31:08 2020

@author: admin
"""
#步驟一


#工件機器限制 K
MachineLimit=[[1,0,1],[1,1,1],[1,0,1],[1,1,1],[1,1,0],
              [1,0,1],[1,1,1],[1,0,1],[0,1,1],[1,1,1]]

#工作時間
Processtime=[[80,0,60],[75,86,94],[25,0,96],[78,95,89],[45,78,0],
              [12,0,65],[55,99,87],[11,0,16],[0,16,45],[43,56,21]]

#指派機器Function
def GetMachineNumber(MachineLimit):
    
    import random
    #選機隨機碼
    SelectJob1=random.random()
    #單份機率
    sum = 0
    for i in MachineLimit:
        sum += i
    PJ1 =1/sum
    #決定是第幾份(k)
    k=1 #<預設為第一份>
    TotalPJ1=PJ1
    while(SelectJob1>TotalPJ1):
        k+=1
        TotalPJ1=PJ1*k
    
    #print(k)
    
    #工作派給機器(j)
    FinalMachineJ1=0
    sequence=[0,1,2]
    for j in sequence:
        if(MachineLimit[j]==1):
            k-=1
        if(k==0):
            FinalMachineJ1=j+1
            break             
    return FinalMachineJ1

#指派10工件
JobResult=[]
for s in MachineLimit:
    JobResult.append(GetMachineNumber(s))
   
#步驟二
#分類依機台
MachineNumber=1
M1=[]
M2=[]
M3=[]
for w in JobResult:
    if(w==1):
        M1.append(MachineNumber)
    elif(w==2):
        M2.append(MachineNumber)
    else:
        M3.append(MachineNumber)
    MachineNumber+=1

#順序隨機碼
import random

\
OrderJob=random.random()

#步驟三



