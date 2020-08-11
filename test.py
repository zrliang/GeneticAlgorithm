#工件機器限制 K
MachineLimit=[[1,0,1],[1,1,1],[1,0,1],[1,1,1],[1,1,0],
              [1,0,1],[1,1,1],[1,0,1],[0,1,1],[1,1,1]]

#工作時間
ProcessTime=[[80,0,60],[75,86,94],[25,0,96],[78,95,89],[45,78,0],
              [12,0,65],[55,99,87],[11,0,16],[0,16,45],[43,56,21]]

#產生染色體
import random
ChromosomeList=[]
JobResult=[]
for i in range(20):
    gene=random.random()
    ChromosomeList.append(gene)

for s in range(10):
    #單份機率
    sum = 0
    for i in MachineLimit[s]:
        sum += i
    PJ1 =1/sum
    #決定是第幾份(k)
    k=1 #<預設為第一份>
    TotalPJ1=PJ1
    while(ChromosomeList[s]>TotalPJ1):
        k+=1
        TotalPJ1=PJ1*k

    #工作派給機器(j)
    FinalMachineJ1=0
    sequence=[0,1,2] #機1.2.3
    for j in sequence:
        if(MachineLimit[s][j]==1):
            k-=1
        if(k==0):
            FinalMachineJ1=j+1 #加回來
            break
    JobResult.append(FinalMachineJ1)

#分類依機台
JobNumber=1
OrderNum=10
M1=[]
M2=[]
M3=[]
OrderJobM1=[]
OrderJobM2=[]
OrderJobM3=[]
i=0
for w in JobResult:
    if(w==1):
        M1.append(JobNumber)
        OrderJobM1.append(ChromosomeList[OrderNum])
    elif(w==2):
        M2.append(JobNumber)
        OrderJobM2.append(ChromosomeList[OrderNum])
    else:
        M3.append(JobNumber)
        OrderJobM3.append(ChromosomeList[OrderNum])
    JobNumber+=1
    OrderNum+=1
print("步驟一")
print(M1)
print(M2)
print(M3)

#步驟二
#決定每個Job在三個機台中的先後順序

def GetMachineJob(M1,OrderJobM1):
    cM1 = list(zip(M1,OrderJobM1))  #兩個一維轉成一個二維
    nM1=sorted(cM1,key=(lambda x:x[1]),reverse=True) #二維排序(x[1]針對欄位二) 由大到小
    nnM1=[]
    for a in range(len(nM1)):
    # print(nM1[a][0]) >> Job幾
        nnM1.append(nM1[a][0])
    return nnM1

FinalM1=GetMachineJob(M1,OrderJobM1)
FinalM2=GetMachineJob(M2,OrderJobM2)
FinalM3=GetMachineJob(M3,OrderJobM3)

print("步驟二")
print(FinalM1)
print(FinalM2)
print(FinalM3)

##--------------------------------要改------------------------------
#步驟三
#計算每個Job的開始與結束時間
print("步驟三")
###---------M1-------

# 開始時間
M1t=0
M1StartAnswer=M1t
M1StartT=[]
M1StartT.append(M1t)
for b in range(len(FinalM1)-1):
   # M1StartT.append(Processtime[nnM1[b]-1][0])
    M1StartAnswer+=ProcessTime[FinalM1[b]-1][0]
    M1StartT.append(M1StartAnswer)

# 結束時間
M1EndAnswer=M1t
M1EndT=[]
for b in range(len(FinalM1)):
   # M1StartT.append(Processtime[nnM1[b]-1][0])
    M1EndAnswer+=ProcessTime[FinalM1[b]-1][0]   #0 [80,0,60] 取第一個欄位
    M1EndT.append(M1EndAnswer)
# 合併
M1Answer = list(zip(FinalM1,M1StartT,M1EndT))
print(M1Answer)


###---------M2-------

# 開始時間
M2t=0
M2StartAnswer=M2t
M2StartT=[]
M2StartT.append(M2t)
for b in range(len(FinalM2)-1):
   # M1StartT.append(Processtime[nnM1[b]-1][0])
    M2StartAnswer+=ProcessTime[FinalM2[b]-1][1]    #1 [80,0,60] 取第二個欄位
    M2StartT.append(M2StartAnswer)

# 結束時間
M2EndAnswer=M2t
M2EndT=[]
for b in range(len(FinalM2)):
   # M1StartT.append(Processtime[nnM1[b]-1][0])
    M2EndAnswer+=ProcessTime[FinalM2[b]-1][1]
    M2EndT.append(M2EndAnswer)
# 合併
M2Answer = list(zip(FinalM2,M2StartT,M2EndT))
print(M2Answer)

###---------M3-------


# 開始時間
M3t=0
M3StartAnswer=M3t
M3StartT=[]
M3StartT.append(M3t)
for b in range(len(FinalM3)-1):
   # M1StartT.append(Processtime[nnM1[b]-1][0])
    M3StartAnswer+=ProcessTime[FinalM3[b]-1][2]    #2 [80,0,60] 取第三個欄位
    M3StartT.append(M3StartAnswer)

# 結束時間
M3EndAnswer=M3t
M3EndT=[]
for b in range(len(FinalM3)):
   # M1StartT.append(Processtime[nnM1[b]-1][0])
    M3EndAnswer+=ProcessTime[FinalM3[b]-1][2]
    M3EndT.append(M3EndAnswer)
# 合併
M3Answer = list(zip(FinalM3,M3StartT,M3EndT))
print(M3Answer)

#-------Makespan----------
#還沒考慮有機器未派到工作之情況

if(M1EndT[-1]>M2EndT[-1] and M1EndT[-1]>M3EndT[-1]):
    Makespan=M1EndT[-1]
elif(M2EndT[-1]>M1EndT[-1] and M2EndT[-1]>M3EndT[-1]):
    Makespan=M2EndT[-1]
else:
    Makespan=M3EndT[-1]

print(Makespan)


#合併



#---------------------
#雙點交配


#單點突變


#畫圖



