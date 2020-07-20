# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 19:31:08 2020

@author: admin
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
print("步驟一")   
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
for x in range(len(M1)):
    OrderJobM1.append(random.random())
cM1 = list(zip(M1,OrderJobM1))  #兩個一維轉成一個二維
nM1=sorted(cM1,key=(lambda x:x[1]),reverse=True) #二維排序(x[1]針對欄位二)
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

print("步驟二")  
# 只取出排序後的工件欄位(nnM?)
nnM1=[]
for a in range(len(nM1)):
   # print(nM1[a][0]) >> Job幾 
    nnM1.append(nM1[a][0])
print(nnM1)
nnM2=[]
 # 工作順序
for a in range(len(nM2)):
   # print(nM1[a][0]) >> Job幾 
    nnM2.append(nM2[a][0])
print(nnM2)
    
nnM3=[]
 # 工作順序
for a in range(len(nM3)):
   # print(nM1[a][0]) >> Job幾 
    nnM3.append(nM3[a][0])
print(nnM3)   
    
    
    
#步驟三
#計算每個Job的開始與結束時間
print("步驟三")  
###---------M1-------

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
    M1EndAnswer+=Processtime[nnM1[b]-1][0]   #0 [80,0,60] 取第一個欄位
    M1EndT.append(M1EndAnswer)
# 合併
M1Answer = list(zip(nnM1,M1StartT,M1EndT))
print(M1Answer)


###---------M2-------


# 開始時間
M2t=0
M2StartAnswer=M2t
M2StartT=[]
M2StartT.append(M2t)
for b in range(len(nnM2)-1):
   # M1StartT.append(Processtime[nnM1[b]-1][0])
    M2StartAnswer+=Processtime[nnM2[b]-1][1]    #1 [80,0,60] 取第二個欄位
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


# 開始時間
M3t=0
M3StartAnswer=M3t
M3StartT=[]
M3StartT.append(M3t)
for b in range(len(nnM3)-1):
   # M1StartT.append(Processtime[nnM1[b]-1][0])
    M3StartAnswer+=Processtime[nnM3[b]-1][2]    #2 [80,0,60] 取第三個欄位         
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

#-------Makespan----------
'''
if(M1Answer>M2Answer and M1Answer>M3Answer):
    print("M1"+" "+ str(M1Answer))
elif(M2Answer>M1Answer and M2Answer>M3Answer):
    print("M2"+" "+ str(M2Answer))
else:
    print("M3"+" "+ str(M3Answer))
''' 

















'''
import random
OrderJobM1=[]
OrderJobM2=[]
OrderJobM3=[]
for x in range(len(M1)):
    OrderJobM1.append(random.random())
cM1 = list(zip(M1,OrderJobM1))  #兩個一維轉成一個二維
nM1=sorted(cM1,key=(lambda x:x[1]),reverse=True) #二維排序
print(nM1)  #排序結果
for x in range(len(M2)):
    OrderJobM2.append(random.random())
cM2 = list(zip(M2,OrderJobM2))  #兩個一維轉成一個二維
nM2=sorted(cM2,key=(lambda x:x[1]),reverse=True) #二維排序
print(nM2)  #排序結果

for x in range(len(M3)):
    OrderJobM3.append(random.random())
cM3 = list(zip(M3,OrderJobM3))  #兩個一維轉成一個二維
nM3=sorted(cM3,key=(lambda x:x[1]),reverse=True) #二維排序
print(nM3)  #排序結果

M1TotalT=0
M2TotalT=0
M3TotalT=0
for a in range(len(nM1)):
   # print(nM1[a][0])
   # AB=Processtime[nM1[a][0]-1][0]
   # print(AB)
    M1TotalT+=Processtime[nM1[a][0]-1][0]
#print(M1TotalT)
    
for a in range(len(nM2)):
    M2TotalT+=Processtime[nM2[a][0]-1][0]
#print(M2TotalT)
    
for a in range(len(nM3)):
    M3TotalT+=Processtime[nM3[a][0]-1][0]
#print(M3TotalT)            

if(M1TotalT>M2TotalT and M1TotalT>M3TotalT):
    print("M1"+" "+ str(M1TotalT))
elif(M2TotalT>M1TotalT and M2TotalT>M3TotalT):
    print("M2"+" "+ str(M2TotalT))
else:
    print("M3"+" "+ str(M3TotalT))

'''
