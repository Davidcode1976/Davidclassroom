# -*- coding:utf-8 -*-
from __future__ import division

scores=[]
title_lst=['名次','姓名','语文','数学','英语','物理','化学','生物','政治','历史','地理','总分','平均分']
account_scores_lst=['平均']

with open('C:\\Users\\Administrator\\PycharmProjects\\Hello\\report.txt','r',encoding='utf-8') as f:
    line_lst=f.readlines()

# 读取成绩文件，生成line_lst列表

for i in line_lst[1:]: # 从第二项开始读取line_lst列表的每一个元素给i
    line=i.split() # 生成单个学生成绩子列表
    single_total=0
    single_avg=0.0

    for score in line[1:]: # 学生成绩子列表中从第二项开始
        single_total+=int(score) # 计算单个学生总分
        single_avg=round(single_total/len(line[1:]),1) # 计算单个学生平均分
    line.append(str(single_total)) # 添加至子列表最后
    line.append(str(single_avg)) # 添加至子列表最后
    scores.append(line) #将每个添加过总分和平均分的子列表添加至scores新列表中

scores=sorted(scores,key=lambda x:x[-1],reverse=True) # 按平均分大小正序排列scores列表

# 设置每个学生科目的循环
for i in range(1,len(scores[1])-1):
    account_total=0 # 科目总分
    account_avg=0 # 科目总平均分

    for j in scores:
        account_total += int(j[i])
        account_avg = account_total // len(scores) #计算总平均分

    account_scores_lst.append(str(account_avg))

account_total_last=0.0
account_avg_last=0.0

for i in scores:
    account_total_last+=float(i[-1])
    account_avg_last=round(account_total_last/len(scores),1)

account_scores_lst.append(str(account_avg_last))
scores.insert(0,account_scores_lst)

for i in range(0,len(scores)):
    scores[i].insert(0,str(i))


for line in range(2,len(scores)):
    for index in range(2,10):
        if int(scores[line][index])<60:
            scores[line][index]='不及格'

scores.insert(0,title_lst)



result=[]

result=[' '.join(i)+'\n' for i in scores]

with open('new_report.txt','w') as f:
    f.writelines(result)






