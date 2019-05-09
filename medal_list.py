# -*- coding:utf-8 -*-

class MedalList():

    def __init__(self,country,gold_medal,silver_medal,bronze_medal):
        self.country=country
        self.gold_medal=gold_medal
        self.silver_medal=silver_medal
        self.bronze_medal=bronze_medal

    def get_place(self,place):
        if place==1:
            self.gold_medal+=1
        elif place==2:
            self.silver_medal+=1
        elif place==3:
            self.bronze_medal+=1

    @property
    def count(self):
        return self.gold_medal+self.silver_medal+self.bronze_medal

    def __str__(self):
        return '%s:金牌%d,银牌%d,铜牌%d,合计:%d' % (self.country,self.gold_medal,self.silver_medal,self.bronze_medal\
                                            ,self.count)

china=MedalList('中国',10,12,21)
us=MedalList('美国',15,18,25)
rus=MedalList('俄罗斯',16,17,24)

print(china)
print(us)
print(rus)
print('中国获得一个亚军:\n')
china.get_place(2)
print(china)
medal_list=[us,rus,china]
print('按金牌数排序:\n')
goldmedal_list=sorted(medal_list,key=lambda x:x.gold_medal,reverse=True)
for i in goldmedal_list:
    print(i)

print('按奖牌数排序:\n')
medalall_list=sorted(medal_list,key=lambda x:x.count,reverse=True)
for j in medalall_list:
    print(j)