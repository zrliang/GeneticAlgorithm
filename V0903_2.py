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
MachineNum=3

    #產生新的機率
def GetInitial():
    import random
    ChromosomeList=[]

    for i in range(ChromosomeLenth):
        gene=random.random()
        ChromosomeList.append(round(gene,5))
    return ChromosomeList

    #產生一條完整染色體
def GetChromosome(ChromosomeList):
    OneChromosome=np.zeros((5,20)) #numpy
    JobResult=[]

    #派機(輪盤法)
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
        sequence=[i for i in range(MachineNum)] #機1.2.3
        for j in sequence:
            if(MachineLimit[s][j]==1):
                k-=1
            if(k==0):
                FinalMachineJ1=j+1 #加回來
                break
        JobResult.append(FinalMachineJ1)

    #工作順序
    machine_list=[]
    order_list=[]
    for k in range(MachineNum+1):
        if(k==0):
            continue
        for i in range(JobNum):
            if(JobResult[i]==k):
                machine_list.append(i+1)
                order_list.append(ChromosomeList[JobNum+i])

        Job_order_=list(zip(machine_list,order_list))  #兩個一維轉成一個二維
        sort_job_=sorted(Job_order_,key=(lambda x:x[1]),reverse=True) #二維排序(x[1]針對欄位二) 由大到小
        for j in range(len(machine_list)):
            OneChromosome[k][j]=sort_job_[j][0]
        machine_list=[]
        order_list=[]

    # 開始結束時間&Makespan
    ##小心各機初始時間
    Job_N=[]
    strT=[]
    temp_str=0 #初始時間
    endT=[]
    temp_end=0
    for i in range(MachineNum+1): #小心 #M1、M2、M3
        if i==0:
            continue
        for s in range(JobNum):
            if(s==0):
                temp_str=0 #換機temp_str從0開始計算
            if(OneChromosome[i][s]!=0):
                Job_N.append(OneChromosome[i][s])
                strT.append(temp_str)
                temp_end=temp_str+ProcessTime[int(OneChromosome[i][s])-1][i-1]
                temp_str=temp_end
                endT.append(temp_end)

    sort_endT=sorted(endT,reverse=False)
    Makespan=sort_endT[-1]

    #最後合併
    a=ChromosomeList
    for i in range(len(a)):
        OneChromosome[0][i]=a[i]

    OneChromosome[4][0]=Makespan

    return OneChromosome
     #GetChromosome(ChromosomeList)


#三維array
import numpy as np
np.set_printoptions(precision=4,suppress=True) #suppress取消科學計數法

#def GetOneGeneration():
#總共50+50

#初始化
PopulationNum=100
TotalChromosome=np.zeros((PopulationNum*2,5,20))
ParentsChromosome=np.zeros((PopulationNum,5,20))
OffspringChromosome=np.zeros((PopulationNum,5,20))
Temp1Chromosome=np.zeros((PopulationNum,5,20))
Temp2Chromosome=np.zeros((PopulationNum,5,20))
FinalChromosome=np.zeros((PopulationNum,5,20))



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
    Matingrate=0.6
    MatingNum=math.ceil(PopulationNum*Matingrate) #無條件進位
    if(MatingNum%2==1):
        MatingNum+=1
    MutationNum=PopulationNum-MatingNum

    #------------------------------------------------------------------

    #交配
    ##任兩條進行交配(一次產生兩條)

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

        #produce offsprings
        Offspring1=GetChromosome(c1)
        Offspring2=GetChromosome(c2)

        Temp1Chromosome[i]=Offspring1
        Temp1Chromosome[i+1]=Offspring2

    #print(Temp1Chromosome)
    #-----------------------------------------------------------------------------
    #單點突變
    ##待

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
    for i in range(0,PopulationNum):
        TotalChromosome[i]=ParentsChromosome[i] #前1/2

    for i in range(0,MatingNum):
        TotalChromosome[i+PopulationNum]=Temp1Chromosome[i]

    for i in range(0,MutationNum):
        TotalChromosome[i+PopulationNum+MatingNum]=Temp2Chromosome[i]


    MakespanOrderIndex=[]
    MakespanOrderValue=[]

    #排序，排序從0-100名

    for i in range(PopulationNum*2):
        MakespanOrderIndex.append(i)
        MakespanOrderValue.append(TotalChromosome[i][4][0]) #[4][0] 固定

    tempMs = list(zip(MakespanOrderIndex,MakespanOrderValue))  #兩個一維轉成一個二維
    OrderMs=sorted(tempMs,key=(lambda x:x[1]),reverse=False) #二維排序(x[1]針對欄位二)


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
    #print(select_index)

    #合併
    ##菁英
    for i in range(eliteN): #10
        FinalChromosome[i]=TotalChromosome[OrderMs[i][0]]
    ##輪盤
    j=eliteN
    for i in select_index: #10-100
        FinalChromosome[j]=TotalChromosome[OrderMs[i+eliteN][0]]
        j+=1

    return FinalChromosome

#print(TotalChromosome[OrderMs[0][0]])

#做100代
#TEST
MakespanRecord=[]
GernerationN=50
MakespanRecord.append(ParentsChromosome[0][4][0])

for i in range(50):
#while(int(MakespanRecord[-1])!=158):
    A=GetOneGeneration(ParentsChromosome)
    ParentsChromosome=A
    MakespanRecord.append(A[0][4][0])
    #GernerationN+=1
    #print(ParentsChromosome[:][:][0:10])


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


#Final time
##開始&結束時間(以上只有工作順序)
Job_N=[]
strT=[]
temp_str=0 #初始時間
endT=[]
temp_end=0
for i in range(MachineNum+1): #小心 #M1、M2、M3
    if i==0:
        continue
    for s in range(JobNum):
        if(s==0):
            temp_str=0 #換機temp_str從0開始計算
        if(ParentsChromosome[0][i][s]!=0):
            Job_N.append(int(ParentsChromosome[0][i][s]))
            strT.append(temp_str)
            temp_end=temp_str+ProcessTime[int(ParentsChromosome[0][i][s])-1][i-1]
            temp_str=temp_end
            endT.append(temp_end)


#畫甘特圖

import plotly.express as px
import datetime
df=[]
m=0
for i in range(len(strT)):
    if(strT[i]==0): #用這判斷
        m+=1
    df.append(dict(Task='Job %s'%Job_N[i],
    Start='2020-07-31 %s'%datetime.timedelta(minutes=strT[i]),
    Finish='2020-07-31 %s'%datetime.timedelta(minutes=endT[i]),Resource='Machine %s'%m))

#呈現圖表
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Task",text="Task")
fig.show()