# -*- coding:utf-8 -*-
from random import randint
import pprint

print()
print('==================\n  这是一个猜数游戏\n==================')
print()

# 姓名 次数 总回合数 最好成绩
# 张三  1     5      5


#　选择进入或退出游戏
while True:
    choice=input('进入游戏选\'Y\',退出请按其他键\n')
    if choice!='Y' and choice!='y':
        break
    else:
        # 打开游戏成绩文件,读取以往记录至score_line
        try:
            with open('C:\\Users\\Administrator\\PycharmProjects\\Hello\\game_score.txt', 'r', encoding='utf-8') as f:
                score_line = f.readlines()

        # 如果没有找到该文件,将score_line初始化
        except:
            score_line = []

        user_name=input('请输入您的姓名:\n')
        # 创建一个game_scores字典，第一项姓名为key
        game_scores = {}
        for i in score_line:
            i_lst = i.split()
            game_scores[i_lst[0]] = i_lst[1:]

        game_score=game_scores.get(user_name)

            # 输入玩家姓名如果不在所有的key中，新人加入
        if user_name not in game_scores.keys():
            print('欢迎\'%s\'加入这个游戏，祝你游戏愉快!'%user_name)
            game_score=[0,0,0]
        else:
            print('欢迎回来\'%s\'，祝你游戏愉快!'%user_name)


        game_rounds=int(game_score[0])
        total_game_times=int(game_score[1])
        min_times=int(game_score[2])
        game_chance = 0  # 设置单次游戏的猜数机会初始值为0

        if game_rounds>0:
            avg_game_times=float(total_game_times)/game_rounds
        else:
            avg_game_times=0

        # 游戏循环，如果玩家结束一次游戏，输入go，就从这里开始再次游戏
        go = False
        while go == False:
            print('猜猜数字是几？')
            num = randint(1, 100)

            user_chance = False
            while user_chance == False:
                game_chance+=1
                print('第 %d 次' % game_chance)

                user_input=False
                while user_input==False:
                    print('请输入100以内的数字')
                    answer=input()
                    try:
                        int(answer)
                    except:
                        continue

                    if int(answer)>100 or int(answer)<0:
                        continue

                    elif int(answer)>num:
                        print('%s 太大了\n'%answer)
                        game_chance+=1
                        print('第 %d 次' % game_chance)
                        continue
                    elif int(answer)<num:
                        print('%s 太小了\n'%answer)
                        game_chance+=1
                        print('第 %d 次' % game_chance)
                        continue
                    elif int(answer)==num:
                        print('猜中了！答案就是 %s'%answer)
                        user_input=True
                # 开始统计数据
                break

            if game_chance<min_times or min_times==0:
                min_times=int(game_chance)

            game_rounds+=1
            total_game_times+=game_chance
            avg_game_times=float(total_game_times)/game_rounds

            print('你猜中答案一共用了 %d 次机会'%game_chance)
            print('你一共玩了 %d 次游戏'%game_rounds)
            print('你平均 %.2f 次猜中答案'%avg_game_times)
            print('你最好成绩是 %d 次'%min_times)
            print

            game_scores[user_name]=[str(game_rounds),str(total_game_times),str(min_times)]

            #pprint.pprint(game_scores)

            #for game_scores_key in game_scores:
                #line = game_scores_key + ' ' + ' '.join(game_scores[game_scores_key])
                #print(line)


            with open('C:\\Users\\Administrator\\PycharmProjects\\Hello\\game_score.txt','w',encoding='utf-8') as j:
                for game_scores_key in game_scores:
                    line=game_scores_key+' '+' '.join(game_scores[game_scores_key])+'\n'
                    j.write(line)

            choice_2=input('输入“go”再玩一次，否则退出游戏\n')
            if choice_2!='go' and choice_2!='GO':
                break
            else:
                print('新游戏')
                game_chance=0
                continue
    print()
    print('==================\n  游戏结束bye bye\n==================')
    print()
    break
















