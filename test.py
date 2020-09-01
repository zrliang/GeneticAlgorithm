
#工件機器限制 K
MachineLimit=[[1,0,1],[1,1,1],[1,0,1],[1,1,1],[1,1,0],
              [1,0,1],[1,1,1],[1,0,1],[0,1,1],[1,1,1]]

#工作時間
ProcessTime=[[80,0,60],[75,86,94],[25,0,96],[78,95,89],[45,78,0],
              [12,0,65],[55,99,87],[11,0,16],[0,16,45],[43,56,21]]

Machine=[[0.2,0.6,0.8,0.7],[4,10,6,0],[5,9,0,0],[3,2,7,0]]
MachineNum=3

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
    for s in range(len(Machine[i])):
        if(s==0):
            temp_str=0 #換機temp_str從0開始計算
        if(Machine[i][s]!=0):
            Job_N.append(Machine[i][s])
            strT.append(temp_str)
            temp_end=temp_str+ProcessTime[Machine[i][s]-1][i-1]
            temp_str=temp_end
            endT.append(temp_end)

sort_endT=sorted(endT,reverse=False)
Makespan=sort_endT[-1]
print(Makespan)


#甘特圖
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



##略
class User:
    def __init__(self,first,last,age):
        self.first=first
        self.last=last
        self.age=age

user1=User("Allen","Liang",20)

#print(user1.age)
