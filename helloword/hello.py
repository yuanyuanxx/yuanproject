# print ("hello word")
# print ("hello word")

# 以end='' 空格为结尾，也可以在里面输入字母，输出结果为ab c
# print('a',end='b ')
# print('c',end='  ')


# age = 3
# name ='xingxing'
# print('{} was {} years old'.format(name, age))

# \n两句语句换行
# print("what's your name?\nMy name is xingxing")

# 通过三引号表达一串双行字符串
# print('''this is the second line."what's your name?",He said "xingxing,pan"''')

# \t 两句子中间加空格
# print("what's your name?\tMy name is xingxing")

# \t 两句子中间加空格
# print("what's your name? My name is xingxing")

# 用r来指定未经过特殊处理的字符串
#  print(r"what's your name? my name \n zhou")


# if 语句
'''number = 16
guess = int(input('Enter an integer: '))
if guess == number:
    print('恭喜你猜对了这个数字')
    print('但是没有礼物')
elif guess < number:
    print('输入的数字太小了')
else:
    print('输入的数字太大了')
print('完成')

#if True: print('yes,it is ture')'''

# while 语句
'''number=16
running=True

while running:
    guess=int(input('输入一个数字'))
    if guess ==number:
        print('恭喜答对了')
        running=False
    elif guess < number:
        print('数字太小了')
    elif guess != number:
        print('数字不对')
    else:
        print('循环结束')'''

# for 循环打印1至7的数字
'''for  i in(range(1,8,6)):
    print(i)

else:
    print('over')'''

# break中断循环
'''while True:
    s=input("输入一些东西:")
    if s=='quit':
        break
    else:
         print("输入的字符长度为",len(s))
print("Done")'''

# continue 当条件不满足时继续循环下一次迭代
'''while True:
    s=input("输入一些内容")
    if s=='quit':
        print("输入内容一致")
        break
    if len(s)<4:
        print("内容太短了")
        continue
    print("输入了足够多的长度")'''

# global 全局变量赋值
'''x=30

def func():
    global x
    print('x is',x)
    x=2
    print('改变全局变量x为',x)
    x=4
    print('改变全局变量x为',x)

func()
print('x的值是',x)'''

# 默认参数值
'''def say(message,time=2):
    print(message * time)

say('Hi')
say('love',8)'''

# 给某些关键字参数
'''
def func(a,b=3,c=5):
    print('a is',a,'b is',b,'c is',c)

func(8,c=4)
func(1,2,3)
func(c=7,a=0)'''

# 参数数量可变
'''
def total(a=3, *numbers, **phonebook):
    print('a=',a)

    for single_item in numbers:
        print('single_item',single_item)
    for first_part,second_part in phonebook.items():
        print(first_part,second_part)

print(total(10,2,788,0,jack=234,john=93949))
'''

# return中断一个函数并返回值
'''
def maximum(x,y):
    if x>y:
        return x
    elif x==y:
        return '两数字是相同'
    else:
        return y
print(maximum(1,3))

'''

# 文档字符串 获取并打印代码注解文本
'''def print_max(x, y):
   #''Prints the maximum of two number.打印两个数值中的最大数。井号后面应该是三个单引号

    # The two values must be integers.'' 此处应该是三个单引号，为了方便注解下段内容就用两个单引号代替
    # 如果可能，将其转换为整数类型
    x=int(x)
    y=int(y)

    if x<y:
        return y
    else:
        return x
print(print_max(8, 3))
#print(max(6,3))
print(print_max.__doc__)'''

# 倒入标准库模块
'''
import sys
print('the command line argument are:')
for i in sys.argv:
    print(i)
print('\n\nThe pythonpath is',sys.path)
'''

# from ..import语句
'''
from math import sqrt
print("Square root of 16 is",sqrt(4))
'''

# 模块__name__
'''
if __name__=='__main__':
    print('this program is being run by itself')
else:
    print('I am being imported from another module')'''

# 数据结构——列表list
'''shoplist=['apple','mango','carrot','banana']
print('I have',len(shoplist),'itmes to purchase.')
print('These items are:',end=' ')
for item in shoplist:
    print(item,end=' ')
print('\n我还需要买大米。')
shoplist.append('rice')
print('现在我需要购买的清单是：',shoplist)

print('I will sort my list now')
shoplist.sort()
#对列表内容进行排序

print('My shopping list is now',shoplist)

print('The first item I will buy is',shoplist[4])
olditem=shoplist[4]
#del shoplist[0]
print('I bought the',olditem)
del shoplist[4]
print('My shopping list is now',shoplist)'''

# 数据结构-元组
'''zoo=('熊猫','天鹅','长颈鹿','大象','猫头鹰')
print('动物园里总共有',len(zoo),'只动物')

new_zoo='猴子','啄木鸟',zoo
print('现在新动物园有',len(new_zoo),'种动物笼子，两个新动物园的笼子，一个旧动物园的笼子')
print('新动物园里有',new_zoo)
print(new_zoo[2],'是从旧的动物园带过来的。')
print('从旧的动物园带过来的最后一个动物是',new_zoo[2][4],)
print('现在新的动物园总共有',len(new_zoo)-1+len(new_zoo[2]),'只动物')'''

# 数据结构-字典
'''ab={
    '星星':'xingxing@126.com',
    '月月':'yueyue@126.com',
    '小阳':'xiaoyang@126.com'
}
print('小阳的邮件地址是：',ab['小阳'])
print('邮件地址是：',ab['小阳'])

del ab['小阳']
print('\n总共有{}个人的联系方式在联系本上'.format(len(ab)))
for name,mailbox in ab.items():
    print('联系 {} \n 通过{}'.format(name,mailbox))
    #print('{} \n {}'.format(name,mailbox))
    #打印出ab字典里所有内容

ab['白云']='baiyun@126.com'
if '白云'in ab:
    print('\n白云的地址是',ab['白云'])
    print('\n现在联系本上有',format(len(ab)),'个人的联系方式')'''

# 数据结构-序列
'''
name='xulie'
print('第0个字符是',name[0])
shoplist=['苹果','芒果','大西瓜','猕猴桃']
print('Item 0 is',shoplist[0])
print('Item 1 is',shoplist[1])
print('Item 2 is',shoplist[2])
print('Item 3 is',shoplist[3])
print('Item -1 is',shoplist[-1])
print('Item -2 is',shoplist[-2])
print('Item -4 is',shoplist[-4])
#通过正序和倒序打印元组里的项目

print('Item 1 to 3 is',shoplist[1:3])
print('Item 2 to end is',shoplist[2:])
print('Item 1 to -1 is',shoplist[1:-1])
print('Item start to end is',shoplist[:])
#通过序列号范围打印元组里范围内的项目

print('xulie 1 to 3 is',name[1:3])
print('xulie 3 to 3 end',name[1:])
print('xulie 1 to -1 is',name[1:-1])
print('xulie start to end is',name[:])
print('xulie start to -1 is',name[:-1])
#从某个字符串中打印部分字符'''

# 数据结构-集合


# 数据结构-引用
'''
print('Simple Assignment')
shoplist=['apple','mango','carrot','banana']
mylist=shoplist

del shoplist[2]

print('shoplist is',shoplist)
print('mylist is',mylist)
#shoplist和mylist指向同一个对象，所以两者打印的内容一致

mylist=shoplist[:]
#mylist赋值一份和shoplist一样的内容
del mylist[1]
#删除mylist元组里一个值
print('shoplist is',shoplist)
print('mylist is',mylist)
#shoplist和mylist是两个独立对象，所以打印的内容不一致。'''

# 关于字符串的内容，检查获取字符串某一部分
'''
name='Swaroop'

if name.startswith('Swa'):
    print('Yes,the string starts with "Swa"')
else:
    print('none')

if 'a'in name:
    print('Yes,it contains the string "a"')

if name.find('war')!=-1:
     print('Yes,it contains the string "war"')
else:
    print('none')
#find 方法用于定位字符串中给定的子字符串的位置。
# 如果找不到相应的子字符串，find 会返回 -1

delimiter='/'

mylist=['上海','北京','深圳','南京']
print(delimiter.join(mylist))
'''

# 类
'''
class Person:
    pass #一个空的代码块
p=Person()
print(p)
'''

# 方法
'''
class Person:
    def say_hi(self):
        print('Hello,how are you')
#p=Person()
#p.say_hi()
#前面两行可以写成如下方式
Person().say_hi()
'''

# __init__方法

'''class Person:
    def __init__(self,name):
        self.name=name

    def say_hi(self):
            print('Hello,my name is',self.name)

p = Person('Swaroop')
p.say_hi()

c=Person('jack')
c.say_hi()
'''

# 字段-类变量与对象变量
'''
class Robot:

    population=0

    def __init__(self,name):

        self.name=name
        print("(Initializing {})".format(self.name))

        Robot.population+=1

    def die(self):
        print("{} is being destroyed!".format(self.name))

        Robot.population-=1
        if Robot.population==0:
           print("{} was the last one.".format(self.name))
        else:
           print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        print("Greetings,my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        print("We have {:d} robots.".format(cls.population))

droid1=Robot("R2-D2")
droid1.say_hi()
Robot.how_many()


droid2=Robot("c2-t2")
droid2.say_hi()
Robot.how_many()

print('\nRobots can do some work here.\n')
print("Robots have finished their work.So let's destory them.")
#droid1.die()
droid2.die()

Robot.how_many()
'''

'''
class Robot:

    population=0

    def __init__(self,name):

        self.name=name
        print("(Initializing {})".format(self.name))

        Robot.population+=1

        print("there are {:d} robot working.".format(Robot.population))

    def die(self):
        print("{} is being destroyed!".format(self.name))

        Robot.population-=1
        if Robot.population==0:
           print("{} was the last one.".format(self.name))
           print("we have {:d} robots working.".format(Robot.population))

        else:
           print("There are still {:d} robots working.".format(Robot.population))




droid1=Robot("R2-D2")
#droid2=Robot("c2-t2")
#droid3=Robot("L2-t2")
print('\n')
droid1.die()
#droid2.die()
#droid3.die()
#Robot.how_many()
'''

# 继承
'''
class SchoolMember:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('Initialized schooleMember:{}'.format(self.name))

    def tell(self):
        print('name "{}",age "{}"'.format(self.name,self.age))

class teacher(SchoolMember):
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary=salary
        print('Initialized Teacher:{}'.format(self.name))

    def tell(self):
            SchoolMember.tell(self)
            print('Salary:"{:d}"'.format(self.salary))

class Student(SchoolMember):
      def __init__(self,name,age,marks):
          SchoolMember.__init__(self,name,age)
          self.marks=marks
          print('(Initialized Student:{})'.format(self.name))

      def  tell(self):
             SchoolMember.tell(self)
             print('Marks:"{:d}"'.format(self.marks))

T=teacher('Mrs.Shrividya',40,30000)
s=Student('Swarpool',25,87)

members=[T,s]

for member in members:
    member.tell()
'''

'''
def is_palindome(text):
    return text==text[::-1]

something=input("Enter text:")
if is_palindome(something):
    print("Yes,it is a palindrome")
else:
    print("No,it is not a palindrome")
'''

# filter函数起过滤作用，对range（500，1000）的item依次执行is_palindrome方法
# range()函数创建一个整数列表
# 切片[::-1]是将列表或字符倒过来
'''
def is_palindrome(n):
    return str(n)==str(n)[::-1]
output=filter(is_palindrome,range(500,1000))
print(list(output))
'''

# 通过file类的对象使用read、readline、write方法打开或使用文件

# poem='''如果你你想让你的工作更快
# 就学习python吧!'''

'''
#打开文件编辑
#open 函数并指定文件名以及我们所希望使用的打开模式
# 来打开一个 文件。打开模式可以是阅读模式( 'r' )，
# 写入模式( 'w' )和追加模式( 'a' )
f=open('poem.txt','w')
#打开文件
f.write(poem)
#关闭文件
#f.close()

#如果没有特别指定，将假定启用默认的阅读模式
f=open('poem.txt')
while True:
    line=f.readline()
    if len(line)==0:
        break
    print(line,end='')

f.close()
'''

# Pickle标准模块将任何纯 Python 对象存储到一
# 个文件中，并在稍后将其取回。这叫作持久地(Persistently)存储对象
'''
import  pickle
#将要储存对象的文件名称
shoplistfile='shoplist.data'
shoplist=['apple','mango','carrot']
#编辑文件
f=open(shoplistfile,'wb')
#将对象转储到文件,调用dump()函数，过程称为封装
pickle.dump(shoplist,f)
f.close()

#删除shoplist变量对象
del shoplist
#从存储中读回
f=open(shoplistfile,'rb')
#从文件中加载对象，调用load（）函数接受返回对象，过程称为拆封
storedlist=pickle.load(f)
print(storedlist)
'''


# 抛出异常
#EOFError没有内建输入，意味着它发现一个不期望的“文件尾”
'''
class ShortInputException(Exception):
    # 一个由用户定义的异常类
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length=length
        self.atleast=atleast
try:
    text=input('Enter something -->')
    if len(text)<3:
        raise ShortInputException(len(text),3)
except EOFError:
    print('Why did you do an EoF on me?')
except ShortInputException as ex:
    print(('ShortInputException:The input was '
    +'{0} long,expected at least {1}').format(ex.length,ex.atleast))
    #输入ascv或abc时，打印'No exception was raised'
else:
    print('No exception was raised.')
'''

#try..finally  在try中获得资源，在 finally 块中释放资源
'''
import time
try:
     f=open('/Users/yuanyuan/PycharmProjects/test.txt','r')
     while True:
        line=f.read()
        if len(line)==0:
            break
        time.sleep(2)
        print (line,end='')
finally:

     f.close()
     print('Cleaning up ....closed the file')
'''

#finally try
'''
import time
try:
     f=open('/Users/yuanyuan/PycharmProjects/test.txt','r')
     while True:
        line=f.read()
        if len(line)==0:
            break
        print (line,end='')
        time.sleep(5)
except IOError:
    print('could not find file!')
except KeyboardInterrupt:
    print('!!You cancelled the reading from the file')

finally:
     f.close()
     print('Cleaning up ....closed the file')

'''
#由filepath获得本地路径的文件，并读取文件内容
'''
import os
filepath=os.path.abspath('/Users/yuanyuan/PycharmProjects/test.txt')
f=open(filepath)
while True:
    line=f.readline()
    if len(line)==0:
        break
    print(line,end='')

f.close()
'''
#read() 一次性读取文本中全部的内容，以字符串的形式返回结果

#readline() 只读取文本第一行的内容，以字符串的形式返回结果

#readlines()  读取文本所有内容，并且以数列的格式返回结果，一般配合for in使用
'''
fh=open('/Users/yuanyuan/PycharmProjects/test.txt','r')
print(fh.readline())
fh.close()

for line in fh.readlines():
    print(line)
'''
'''
a=open(r'/Users/yuanyuan/PycharmProjects/test.txt')
a.seek(0)
print(a.read())
'''

#读取文件时避免忘记或者为了避免每次都要手动关闭文件，可以使用with语句
with open('/Users/yuanyuan/PycharmProjects/test.txt','r') as f:
    print(f.read())
print(f.closed)
