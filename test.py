# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#步驟一
#將每個Job 亂數指派到Machine 1~3之一

#工件機器限制 K
MachineLimit=[[1,0,1],[1,1,1],[1,0,1],[1,1,1],[1,1,0],
              [1,0,1],[1,1,1],[1,0,1],[0,1,1],[1,1,1]]

#工作時間
Processtime=[[80,0,60],[75,86,94],[25,0,96],[78,95,89],[45,78,0],
              [12,0,65],[55,99,87],[11,0,16],[0,16,45],[43,56,21]]


#指派機器Function
def GetMachineNumber(MachineLimit):
    
    #選機隨機碼
    import random
    SelectJobCode=random.random() #0~1亂數
    #單份機率
    sum = 0
    for i in MachineLimit:
        sum += i
    PJ1 =1/sum
    #決定是第幾份(k)
    k=1 #<預設為第一份>
    TotalPJ1=PJ1
    while(SelectJobCode>TotalPJ1):
        k+=1
        TotalPJ1=PJ1*k
    
    #print(k)
    
    #工作派給機器(j)
    FinalMachineJ1=0
    sequence=[0,1,2] #機1.2.3
    for j in sequence:
        if(MachineLimit[j]==1):
            k-=1
        if(k==0):
            FinalMachineJ1=j+1 #加回來
            break             
    return FinalMachineJ1

##(呼叫Function)指派10工件給3機
JobResult=[]
for s in MachineLimit:
    JobResult.append(GetMachineNumber(s)) #參數 工件一:[1,0,1]...

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
print(M1)
print(M2)
print(M3)

#步驟二
#決定每個Job在三個機台中的先後順序
 
#產生順序隨機碼，進行排序
import random
OrderJobM1=[]
OrderJobM2=[]
OrderJobM3=[]

Machine=[]
Machine.append(M1)
Machine.append(M2)
Machine.append(M3)
def GetMachineJobOrder(M1):
    for x in range(len(M1)):
        OrderJobM1.append(random.random())
    cM1 = list(zip(M1,OrderJobM1))  #兩個一維轉成一個二維
    nM1=sorted(cM1,key=(lambda x:x[1]),reverse=True) #二維排序(x[1]針對欄位二)
    #print(nM1)  #排序結果
    return nM1

OrderResult=[]
for q in Machine:
    OrderResult.append(GetMachineJobOrder(q))
print(OrderResult)
# 只取出排序後的工件欄位(nnM?)
nnM1=[]
for a in range(len(nM1)):
   # print(nM1[a][0]) >> Job幾 
    nnM1.append(nM1[a][0])

nnM2=[]
 # 工作順序
for a in range(len(nM2)):
   # print(nM1[a][0]) >> Job幾 
    nnM2.append(nM2[a][0])
#print(nnM1)
    
nnM3=[]
 # 工作順序
for a in range(len(nM3)):
   # print(nM1[a][0]) >> Job幾 
    nnM3.append(nM3[a][0])
#print(nnM1)   