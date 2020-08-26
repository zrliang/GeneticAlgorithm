
#工件機器限制 K
MachineLimit=[[1,0,1],[1,1,1],[1,0,1],[1,1,1],[1,1,0],
              [1,0,1],[1,1,1],[1,0,1],[0,1,1],[1,1,1]]

#工作時間
ProcessTime=[[80,0,60],[75,86,94],[25,0,96],[78,95,89],[45,78,0],
              [12,0,65],[55,99,87],[11,0,16],[0,16,45],[43,56,21]]

M1=[4,10,6]
M2=[5,9]
M3=[3,2,7]


strT=[]
endT=[]






class User:
    def __init__(self,first,last,age):
        self.first=first
        self.last=last
        self.age=age

user1=User("Allen","Liang",20)

print(user1.age)
