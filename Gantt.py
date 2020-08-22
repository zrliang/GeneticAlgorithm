## Gantt

#M1Answer、M2Answer、M3Answer要改成你的各機器做出來的時間
'''

M1Answer=[(3,0,25),(2,25,100),(6,100,112),(7,112,167)]
(工件編號,開始時間,結束時間)
代表機器一有3,2,6,7的工件要做...

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
'''
這個給你參考，官方文件的範例
df = pd.DataFrame([
    dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Resource="Alex"),
    dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource="Alex"),
    dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Resource="Max")
])
'''
#呈現圖表
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Task",text="Task")
fig.show()