#工件機器限制 K
MachineLimit=[[1,0,1],[1,1,1],[1,0,1],[1,1,1],[1,1,0],
              [1,0,1],[1,1,1],[1,0,1],[0,1,1],[1,1,1]]

#工作時間
ProcessTime=[[80,0,60],[75,86,94],[25,0,96],[78,95,89],[45,78,0],
              [12,0,65],[55,99,87],[11,0,16],[0,16,45],[43,56,21]]

JobNum=10
ChromosomeLenth=JobNum*2
MachineNum=3

    #產生新的機率(ok)

import random
ChromosomeList=[]

for i in range(ChromosomeLenth):
    gene=random.random()
    ChromosomeList.append(round(gene,5))


import numpy as np
OneChromosome=np.zeros((5,20))

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
    sequence=[i for i in range(MachineNum)] #機1.2.3
    for j in sequence:
        if(MachineLimit[s][j]==1):
            k-=1
        if(k==0):
            FinalMachineJ1=j+1 #加回來
            break
    JobResult.append(FinalMachineJ1)

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

print(OneChromosome)
a=ChromosomeList

#e=MakespanList
'''
for i in range(len(a)):
    OneChromosome[0][i]=a[i]

for i in range(len(e)):
    OneChromosome[4][i]=e[i]
'''