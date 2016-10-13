import pymongo
from numpy import *
import os

client = pymongo.MongoClient('localhost',27017)
MiddleSchoolProject = client['MiddleSchoolProject']
high2011Score = MiddleSchoolProject['high2011Score']

for item in high2011Score.find().limit(30):
     pass

Scorelist=[]
for item in high2011Score.find():
    try:
        wen = (float(item['语文1'])+float(item['英语1'])+float(item['历史1']) \
               +float(item['地理1'])+float(item['政治1']))/5
        li = (float(item['数学1'])+float(item['物理1'])+float(item['化学1'])+float(item['生物1']))/4
        distPerson = sqrt(power(wen-li,2))
        Scorelist.append(['姓名：',item['姓名'],'文理成绩欧拉距离：',distPerson])
    except:
        continue

sortedList = sorted(Scorelist,key=lambda d:d[3],reverse=False)
for person in range(len(sortedList)):
    print('文理均衡名次'+str(person+1),end=' ')
    print(sortedList[person][0],end=' ')
    print(sortedList[person][1],end=' ')
    print(sortedList[person][2],end=' ')
    print(sortedList[person][3],end='\n')


path = './test'
if not os.path.exists(path):
    os.mkdir(path)
with open(os.path.join(path,'wenli.txt'),'w') as _file:
    _file.write('文理科排名的初步分析')
    _file.write('\n'+"*****************"+'\n')
    for person in range(len(sortedList)):
        _file.write('文理均衡名次' + str(person + 1)+' '+str(sortedList[person][1])+' '+str(sortedList[person][2])+' '+str(sortedList[person][3]))
        _file.write('\n')

print('yeal!')