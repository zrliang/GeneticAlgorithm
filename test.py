# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
Processtime=[[80,0,60],[75,86,94],[25,0,96],[78,95,89],[45,78,0],
              [12,0,65],[55,99,87],[11,0,16],[0,16,45],[43,56,21]]

cM1=[]
M1=[5,6]
import random
OrderJobM1=[]
for x in range(len(M1)):
    OrderJobM1.append(random.random())
cM1 = list(zip(M1,OrderJobM1))  #兩個一維轉成一個二維
nM1=sorted(cM1,key=(lambda x:x[1]),reverse=True) #二維排序


print(Processtime[:][0])


