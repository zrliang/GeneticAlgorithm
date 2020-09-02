#工件機器限制 K
MachineLimit=[[1,0,1],[1,1,1],[1,0,1],[1,1,1],[1,1,0],
              [1,0,1],[1,1,1],[1,0,1],[0,1,1],[1,1,1]]

#工作時間
ProcessTime=[[80,0,60],[75,86,94],[25,0,96],[78,95,89],[45,78,0],
              [12,0,65],[55,99,87],[11,0,16],[0,16,45],[43,56,21]]

JobNum=10
ChromosomeLenth=JobNum*2
MachineNum=3

#def GetOneGeneration():
#總共50+50

#初始化
import numpy as np
np.set_printoptions(precision=4,suppress=True)
PopulationNum=50
TotalChromosome=np.zeros((PopulationNum*2,5,20))
ParentsChromosome=np.zeros((PopulationNum,5,20))
OffspringChromosome=np.zeros((PopulationNum,5,20))
Temp1Chromosome=np.zeros((PopulationNum,5,20))
Temp2Chromosome=np.zeros((PopulationNum,5,20))
Temp_rank_Chromosome=np.zeros((PopulationNum,5,20))
FinalChromosome=np.zeros((PopulationNum,5,20))

TestChromosome=np.zeros((50,5,20))

#產生新的機率(ok)

def GetInitial():
    import random
    ChromosomeList=[]

    for i in range(ChromosomeLenth):
        gene=random.random()
        ChromosomeList.append(round(gene,5))
    return ChromosomeList

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

        print(machine_list)
        print(sort_job_)
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

#母體
##產生第一次母代50條的染色體
GetChromosome(GetInitial())