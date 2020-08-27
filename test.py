
#工件機器限制 K
MachineLimit=[[1,0,1],[1,1,1],[1,0,1],[1,1,1],[1,1,0],
              [1,0,1],[1,1,1],[1,0,1],[0,1,1],[1,1,1]]

#工作時間
ProcessTime=[[80,0,60],[75,86,94],[25,0,96],[78,95,89],[45,78,0],
              [12,0,65],[55,99,87],[11,0,16],[0,16,45],[43,56,21]]

Machine=[[0.2,0.6,0.8,0.7],[4,10,6,0],[5,9,0,0],[3,2,7,0]]

MachoneNum=3

Job_N=[]
strT=[]
temp_str=0 #初始解
endT=[]
temp_end=0
for i in range(MachoneNum+1): #小心
    if i==0:
        continue
    for s in range(len(Machine[i])):
        if(Machine[i][s]!=0):
            Job_N.append(Machine[i][s])
            strT.append(temp_str)
            temp_end=temp_str+ProcessTime[Machine[i][s]-1][i-1]
            temp_str=temp_end
            #strT.append(temp_str)
            endT.append(temp_end)

            #print(temp_str)
print(Job_N)
print(strT)
print(endT)




'''
import plotly.express as px
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




class User:
    def __init__(self,first,last,age):
        self.first=first
        self.last=last
        self.age=age

user1=User("Allen","Liang",20)

#print(user1.age)
