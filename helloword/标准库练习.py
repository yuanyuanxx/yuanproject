#sys 模块
'''import sys
print(sys.version_info)
#输出 sys.version_info(major=3,minor=5,micro=1,releaselevel='final',serial=0)
if sys.version_info.major==3:
        print ('Yes!')

'''
#日志模块
'''
import os #os 模块用以和操作系统交互
import platform #获取平台——操作系统的信息
import logging #记录log信息

if platform.platform().startswith('Windows'):
   logging_file=os.path.join(os.getenv('HOMEDRIVER'),os.getenv('HONEPATH'),'test.log')
else:
    logging_file=os.path.join(os.getenv('HOME'),'test.log')
print('Logging to',logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    #filename=logging_file,
    filemode='w',
)
logging.debug('Start of the program')
logging.info('Doing something')
logging.warning('Dying now')
'''
#传递元组
'''
def get_error_details():
    return(2,'detailx')

errnum,errstr=get_error_details()
print(errnum)
print(errstr)
'''

#交换两个变量最快的方式
'''
a=2;b=9
print(a,b)
a,b=b,a
print(a,b)
'''
#Lambda表格 创建一个新的函数对象
#list 的 sort 方法可以获得一个 key 参数
'''
points=[{'x':4,'y':6},
        {'x':8,'y':5}]
#points.sort(key=lambda i:i['a'])
points.sort(key=lambda i: i['y'])
print(points)
#print(b)
'''
#map函数返回的是一个迭代器，map函数将会把函数应用在可迭代对象迭代出的每一个值上。
'''
items=[1,2,3,4,5]
squared=list(map(lambda x:x**2,items))
print(squared)
'''
#将lambda和map同时使用一个函数列表。
'''def multiply(x):
    return (x*x)
def add(x):
    return(x+x)

funcs=[multiply,add]
for i in range(5):
    value=list(map(lambda x: x(i),funcs))
    print(value)
'''
#序列取值
'''
points=[{'x':3,'y':6},
        {'x':7,'y':9}]
print (points[:])
print (points[1:2])
print (points[0:1])
#for in if
'''
#打印出能被3整除的数字
'''
foo=[2,18,19,22,17,24,8,12,27]
for g in foo:
    if g%3==0:
        print(g)
'''
#列表推导：一份数据列表中，获得数字大于2的情况下乘以2的新列表
'''
listone=[1,3,6]
listtwo=[2*i for i in listone if i>2]
print(listtwo)
'''

#*args 是多个变量组成的list. 函数中接收元组与字典，函数需要一个可变数量的实参时，

'''
def powersum(power,*args):
    total=0
    for i in args:
        total+=pow(i,power)     #pow()乘方
        return total
#print(powersum(2,10))  #输出100 （10的2次方）
print(powersum(2,3,4)) #结果输出9，应该输出25  （3的2次方+4的2次方）
#print(powersum(2,3,4))
'''

#*args,**kwargs用于函数的参数不确定的时候,分别使用
# *或**作为元组或字典前缀，使它作为一个参数为函数接收.
'''
def foo(*args,**kwargs):
    print('args=',args)
    print('kwargs=',kwargs)
    print('____________________')
if __name__=='__main__':
  #if __name__ == '__main__'的意思是：当.py文件被直接运行时，
#  if __name__ == '__main__'之下的代码块将被运行；当.py文
# 件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
    print(foo(1,2,3))
    print(foo(a=2,b=4,c=6))
    print(foo(1,2,3,a=1,b=2,c=3))
    print(foo('a',1,None,a=1,b=2,c=3))
'''
#装饰器<有些地方不是很理解>
'''
from time import sleep
from functools import wraps
import logging

logging.basicConfig()
#获取logger实例，如果参数为空则返回root
log=logging.getLogger('retry')

def retry(f):
    @wraps(f)
    def wrapped_f(*args,**kwargs):
        max_attempts=5
        for attemp in range(1,max_attempts+1):
            try:
                return f(*args,**kwargs)
            except:
                log.exception("attempt %s/%s failed:%s",
                              attempt,
                              max_attempts,
                              (args,kwargs))
                time.sleep(10 * attempt)
        log.critical('All %s attempts failed :%s',
                             max_attempts,
                             (args,kwargs))
    return wrapped_f

counter=0

@retry
def save_to_database(arg):
        print('写入数据库或进行网络通话.')
        print('如果发生异常，这将自动重试.')
        global counter
        counter+=1
        # 这将在第一次调用时抛出异常
        # 在第二次运行时将正常工作(也就是重试)
        if counter<2:
            raise ValueError(arg)
if __name__=='__main__':
        save_to_database('Some bad value')
'''
#装饰器 functools.wraps
#实现一个函数执行后计算执行时间的功能
#import time,functools
'''
def foo():
    print('this is foo!')
foo()

#查看函数执行时间
def foo1():
    start_time=time.clock()
    print('this is foo1.')
    end_time=time.clock()
    print('执行的时间为:',end_time-start_time)
foo1()
'''
'''
def foo3():
    print('this is foo3')

def timeit(func):
    #重新定义一个函数timeit，将foo3的引用传递给他
    #在timeit中调用foo3并进行计时，这样，我们就达到了不改动foo3定义的目的
    #param func：传入的函数
    start_time=time.clock()
    func()   #等同于foo3()，输出'this is foo3'
    end_time=time.clock()
    print('used:',end_time-start_time)
timeit(foo3)
'''

'''
def timeit4(func):
    #@functools.wraps(func)
    #定义一个内嵌的包装函数，给传入的函数加上计时功能包装
    def wrapper():
        start_time=time.clock()
        func()
        end_time=time.clock()
        print('used:',end_time-start_time)
    #将包装后的函数返回
    return wrapper
#---------以上代码就类似装饰器————————
@timeit4
def foo4():
    #return None
    print('this is foo4.')
foo4()
'''
