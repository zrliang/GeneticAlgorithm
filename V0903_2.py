import time
start = time.process_time() #計算執行時間


#工件機器限制 K
MachineLimit=[[1,0,1],[1,1,1],[1,0,1],[1,1,1],[1,1,0],
              [1,0,1],[1,1,1],[1,0,1],[0,1,1],[1,1,1]]

#工作時間
ProcessTime=[[80,0,60],[75,86,94],[25,0,96],[78,95,89],[45,78,0],
              [12,0,65],[55,99,87],[11,0,16],[0,16,45],[43,56,21]]

JobNum=10
ChromosomeLenth=JobNum*2
MachoneNum=3

    #產生新的機率(ok)
def GetInitial():
    import random
    ChromosomeList=[]

    for i in range(ChromosomeLenth):
        gene=random.random()
        ChromosomeList.append(round(gene,5))
    return ChromosomeList

    #產生一條完整染色體(ok)
def GetChromosome(ChromosomeList):
    JobResult=[]

    #輪盤法
    for s in range(JobNum): #Job數
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
        sequence=[i for i in range(MachoneNum)] #機1.2.3
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

    #print("步驟一")
    #print(M1)
    #print(M2)
    #print(M3)

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

    #print("步驟二")
    #print(FinalM1)
    #print(FinalM2)
    #print(FinalM3)

    ##--------------------------------要改------------------------------
    #步驟三
    #計算每個Job的開始與結束時間

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
    M1EndT=[0]
    for b in range(len(FinalM1)):
    # M1StartT.append(Processtime[nnM1[b]-1][0])
        M1EndAnswer+=ProcessTime[FinalM1[b]-1][0]   #0 [80,0,60] 取第一個欄位
        M1EndT.append(M1EndAnswer)
    # 合併
    M1Answer = list(zip(FinalM1,M1StartT,M1EndT))
    #print(M1Answer)


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
    M2EndT=[0]
    for b in range(len(FinalM2)):
    # M1StartT.append(Processtime[nnM1[b]-1][0])
        M2EndAnswer+=ProcessTime[FinalM2[b]-1][1]
        M2EndT.append(M2EndAnswer)
    # 合併
    M2Answer = list(zip(FinalM2,M2StartT,M2EndT))
    #print(M2Answer)

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
    M3EndT=[0]
    for b in range(len(FinalM3)):
    # M1StartT.append(Processtime[nnM1[b]-1][0])
        M3EndAnswer+=ProcessTime[FinalM3[b]-1][2]
        M3EndT.append(M3EndAnswer)
    # 合併
    M3Answer = list(zip(FinalM3,M3StartT,M3EndT))
    #print(M3Answer)

    #-------Makespan----------
    #考慮有機器未派到工作之情況(EndT 先加一個0)

    #決定makespan比大小
    EndTList=[]
    EndTList.append(M1EndT[-1])
    EndTList.append(M2EndT[-1])
    EndTList.append(M3EndT[-1])

    OrderEndT=sorted(EndTList,reverse=True) #由大到小
    Makespan=OrderEndT[0]

    MakespanList=[]
    MakespanList.append(Makespan)
    #print(Makespan)

    a=ChromosomeList
    b=FinalM1
    c=FinalM2
    d=FinalM3
    e=MakespanList
    import numpy as np
    OneChromosome=np.zeros((5,20))
    for i in range(len(a)):
        OneChromosome[0][i]=a[i]
    for i in range(len(b)):
        OneChromosome[1][i]=b[i]
    for i in range(len(c)):
        OneChromosome[2][i]=c[i]
    for i in range(len(d)):
        OneChromosome[3][i]=d[i]
    for i in range(len(e)):
        OneChromosome[4][i]=e[i]

    return OneChromosome #產生特定一條染色體，機率須給定
                          #GetChromosome(ChromosomeList)
#三維array
import numpy as np
np.set_printoptions(precision=4,suppress=True) #suppress取消科學計數法

#def GetOneGeneration():
#總共50+50

#初始化
PopulationNum=50
TotalChromosome=np.zeros((PopulationNum*2,5,20))
ParentsChromosome=np.zeros((PopulationNum,5,20))
OffspringChromosome=np.zeros((PopulationNum,5,20))
Temp1Chromosome=np.zeros((PopulationNum,5,20))
Temp2Chromosome=np.zeros((PopulationNum,5,20))
Temp_rank_Chromosome=np.zeros((PopulationNum,5,20))
FinalChromosome=np.zeros((PopulationNum,5,20))

TestChromosome=np.zeros((50,5,20))

#母體
##產生第一次母代50條的染色體
for i in range(PopulationNum):
    ParentsChromosome[i]=GetChromosome(GetInitial()) ##Getinitial

#OffspringChromosome[:]=ParentsChromosome[:]

def GetOneGeneration(ParentsChromosome):
    OffspringChromosome[:]=ParentsChromosome[:]
    #---------------------
    #交配率(交配&突變)
    import math
    PopulationNum=50
    Matingrate=0.01
    MatingNum=math.ceil(PopulationNum*Matingrate) #無條件進位
    if(MatingNum%2==1):
        MatingNum+=1
    #Question

    #Question
    MutationNum=PopulationNum-MatingNum

    #------------------------------------------------------------------

    #交配
    ##任兩條進行交配(一次產生兩條)

    #tempMateNum單數不適用!!!!

    even = [i-1 for i in range(1,MatingNum) if i %2==1] #tempMateNum決定要做幾次(3次>>產生6條子代)

    for i in even:
        #任選兩條
        import random
        size=range(1,1+PopulationNum)  #母體大小

        AnyTwo=random.sample(size, 2)
        AnyTwo.sort()
        #print(AnyTwo)

        FirstC=AnyTwo[0]-1 #index
        SecondC=AnyTwo[1]-1
        #print(FirstC,SecondC)

        p1=OffspringChromosome[FirstC][0].tolist()
        p2=OffspringChromosome[SecondC][0].tolist()

        # 雙點交配
        CutPoint=[]
        size=range(1,21)  #染色體大小 #10+10(range(1,21))

        CutPoint=random.sample(size, 2)
        CutPoint.sort()
        #print(CutPoint)

        strpoint=CutPoint[0]
        endpoint=CutPoint[1]

        c1=p1[:]
        c2=p2[:]

        c1[strpoint-1:endpoint]=p2[strpoint-1:endpoint]
        c2[strpoint-1:endpoint]=p1[strpoint-1:endpoint]

        #print(c1)
        #print(c2)

        #produce offsprings
        Offspring1=GetChromosome(c1)
        Offspring2=GetChromosome(c2)

        Temp1Chromosome[i]=Offspring1
        Temp1Chromosome[i+1]=Offspring2

    #print(Temp1Chromosome)
    #-----------------------------------------------------------------------------
    #單點突變
    ##待

    #決定要做幾次

    import random
    #任選一條
    size1=range(0,PopulationNum)
    #print(size1)
    AnyChros=random.sample(size1, MutationNum) ##產生被挑中的染色體清單(size,產生幾個)
    #print(AnyOne)

    for i in range(MutationNum):
        size2=range(0,20) #基因數
        AnyGene=random.sample(size2,1) #list
        #print(AnyGene)
        prob=OffspringChromosome[AnyChros[i]][0].tolist()
        #print(p1)
        NewProb=random.random()
        prob[AnyGene[0]]=round(NewProb,5)
        #print(p1)

        OffspringMutation=GetChromosome(prob)
        Temp2Chromosome[i]=OffspringMutation

    #print(Temp2Chromosome)

    #合併

    #以上暫時

    for i in range(0,PopulationNum):
        TotalChromosome[i]=ParentsChromosome[i] #前1/2

    for i in range(0,MatingNum):
        TotalChromosome[i+PopulationNum]=Temp1Chromosome[i]

    for i in range(0,MutationNum):
        TotalChromosome[i+PopulationNum+MatingNum]=Temp2Chromosome[i]

    #print(TotalChromosome)

    MakespanOrderIndex=[]
    MakespanOrderValue=[]

    #排序，排序從0-100名

    for i in range(PopulationNum*2):
        MakespanOrderIndex.append(i)
        MakespanOrderValue.append(TotalChromosome[i][4][0]) #[4][0] 固定

    tempMs = list(zip(MakespanOrderIndex,MakespanOrderValue))  #兩個一維轉成一個二維
    OrderMs=sorted(tempMs,key=(lambda x:x[1]),reverse=False) #二維排序(x[1]針對欄位二) 由大到小


    #rate
    eliteN=int(PopulationNum*0.1) #10
    rankN=PopulationNum-eliteN #40
    rank_rangeN=PopulationNum*2-eliteN #90

    #等級輪盤制
    def sum(num): #分母
        sum = 0
        x=1
        while x < num+1:
            sum = sum + x
            x+=1
        return sum
    Sum=sum(rank_rangeN) #1+2+..+90

    t=0
    proba_list=[0]
    for i in range(rank_rangeN-1):
        proba=(rank_rangeN-i)/Sum #90/1+...
        t+=proba
        proba_list.append(t)
    #print(proba_list)

    def getk2(): #得index
        import random
        selectone=random.random()
        k2=-1
        for i in range(len(proba_list)):
            if(selectone>proba_list[i]):
                k2+=1
        return k2

    select_index=[]
    count=0
    while(len(select_index)<rankN): #不重複 #40個
        count+=1
        temp=getk2()
        if(temp not in select_index):
            select_index.append(temp)
    #print(count)
    #測試
    #OrderMsAA=sorted(select_index,reverse=False)
    #print(OrderMsAA)

    #合併
    ##菁英
    for i in range(eliteN): #10
        FinalChromosome[i]=TotalChromosome[OrderMs[i][0]]
    ##輪盤法
    j=eliteN
    for i in select_index: #10-100
        FinalChromosome[j]=TotalChromosome[OrderMs[i+eliteN][0]]
        j+=1

    return FinalChromosome

#print(TotalChromosome[OrderMs[0][0]])

#做100代

#MakespanRecord=[]
#for i in range(10):
#    A=GetOneGeneration(ParentsChromosome)
#    ParentsChromosome=A
 #   MakespanRecord.append(A[0][4][0])

#print(A[0:3])


MakespanRecord=[]
GernerationN=0
MakespanRecord.append(ParentsChromosome[0][4][0])

for i in range(100):
    A=GetOneGeneration(ParentsChromosome)
    ParentsChromosome=A
    MakespanRecord.append(A[0][4][0])
    GernerationN=i+1
print(A)



#時間內做完
'''
MakespanRecord=[]
GernerationN=0
pt=float(input("欲執行秒數:")) #input

for i in range(15000): #最多15000代
    A=GetOneGeneration(ParentsChromosome)
    ParentsChromosome=A
    print(A)
    MakespanRecord.append(A[0][4][0])
    end = time.process_time()
    processT=end-start
    GernerationN=i+1
    if(processT>=pt): #1秒
        break
 '''

#收斂圖

import matplotlib.pyplot as plt

plt.plot([i for i in range(len(MakespanRecord))],MakespanRecord,'b') #x,y為list資料
plt.ylabel('makespan',fontsize=15)
plt.xlabel('generation',fontsize=15)
plt.show()


# 輸出結果
print(str(GernerationN)+"代")
print(MakespanRecord[-1])
#print("執行時間：%f 秒" % (end - start))


#算出開始&結束時間(以上只有工作順序)


#畫甘特圖
'''
print(A[0])
for i in range(10):
    if(A[0][1][i]!=0):
        print(int(A[0][1][i]))
'''

'''
import plotly.express as px
import pandas as pd
import datetime

df=[]
#M1
# Task放工件編號; Start&Finish分別放各工件的開始與結束時間，
# 初始時間需先給定一個時間格式 ex: 2020-07-31 分鐘格式 ，我這邊是利用datetime.timedelta(minutes=)將工作時間轉成分鐘
# Resource 放機器分類

for i in range(len(M1Answer)):
    df.append(dict(Task='Job %s'%M1Answer[i][0], Start='2020-07-31 %s'%datetime.timedelta(minutes=M1Answer[i][1]),
    Finish='2020-07-31 %s'%datetime.timedelta(minutes=M1Answer[i][2]),Resource='Machine 1'))

#M2
for i in range(len(M2Answer)):
    df.append(dict(Task='Job %s'%M2Answer[i][0], Start='2020-07-31 %s'%datetime.timedelta(minutes=M2Answer[i][1]),
    Finish='2020-07-31 %s'%datetime.timedelta(minutes=M2Answer[i][2]),Resource='Machine 2'))

#M3
for i in range(len(M3Answer)):
    df.append(dict(Task='Job %s'%M3Answer[i][0], Start='2020-07-31 %s'%datetime.timedelta(minutes=M3Answer[i][1]),
    Finish='2020-07-31 %s'%datetime.timedelta(minutes=M3Answer[i][2]),Resource='Machine 3'))

#呈現圖表
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Task",text="Task")
fig.show()
'''





