# -*- coding:utf-8 -*-

def load_blocked():#定义读取屏蔽词函数
    with open('C:\\Users\\Administrator\\PycharmProjects\\Hello\\ciku.txt') as f:
        global blocked_words#设定该变量为全局变量
        blocked_words=[]
        lines=f.readlines()

        for index in lines:
              if index:  #如果index不是空字符，去掉首尾的空格
                     index=index.strip()
                     blocked_words.append(index)

def words_filter(text,charset='utf-8',symbol='*'):#定义替换屏蔽词函数，参数为输入的文本和utf-8编码和替换符号，
    # 其中utf-8编码和替换符号是默认参数
    for w in blocked_words:
        text=text.replace(w,symbol*len(w.decode(charset)))#用decode对中文解码并计算字符长度
    return text

if __name__=='__main__':
    load_blocked()
    while True:
        user_input=raw_input('请输入一段文字：\n')
        if not user_input:#如果输入不是空字符，则输出替换结果
            break
        print words_filter(user_input)