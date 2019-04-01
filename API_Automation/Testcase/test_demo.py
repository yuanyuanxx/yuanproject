# -*- coding:utf-8 -*-
import os
import random
def test_demo1():
    a={'a':1,'v':2,'d':3,'t':4}
    print(a.get('s'))
    c=a.pop('t')
    print(c)
    print(a)

def test_demo2():
    a=[1,3,5]
    if isinstance(a,list):
        return print('YEs')
    else:
        return print('no')

#判断2-100中哪些是素数
def test_demo3():
    i = 2
    while (i < 100):
        j = 2
        while (j <= (i / j)):
            if not (i % j):
                break
            j = j + 1
        if (j > i / j):
            print(i, " 是素数")
        i = i + 1
    print ("Good bye!")

def test_demo4():
    print("当前工作目录：%s" % os.getcwd())

def test_demo5():
    articleInfo = [{"tid": 101115, "lang": "en", "subjectId": 1043},
                        {"tid": 101111, "lang": "jp", "subjectId": 1050},
                        {"tid": 101133, "lang": "kr", "subjectId": 1056}
                   ]
    # i=random.randint(0,3)
    # print(i)
    artinfo=articleInfo[2]
    print(artinfo)
    lang=artinfo["lang"]
    print(lang)



'''
def test_demo2():
    dictionary = {}
    flag = 'a'
    pape = 'a'
    off = 'a'
    while flag == 'a' or 'c' :
        flag = input("添加或查找单词 ?(a/c)")
        if flag == "a" :                             # 开启
            word = input("输入单词(key):")
            defintion = input("输入定义值(value):")
            dictionary[str(word)] = str(defintion)  # 添加字典
            print ("添加成功!")
            pape = input("您是否要查找字典?(a/0)")   #read
            if pape == 'a':
                print (dictionary)
            else :
                continue
        elif flag == 'c':
            check_word = input("要查找的单词:")  # 检索
            for key in sorted(dictionary.keys()):            # yes
                if str(check_word) == key:
                    print ("该单词存在! ",key, dictionary[key])
                    break
                else:                                       # no
                    off = 'b'
            if off == 'b':
                print ("抱歉，该值不存在！")
        else:                               # 停止
            print ("error type")
            break
'''


