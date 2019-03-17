import pytest
import time
import csv
'''
#带参数的fixture，写法一
@pytest.fixture(params=[{'username':'test1','password':'1'},
                        {'username':'test2','password':'2'}])
def daccout_provider(request):
    return request.param
def test_login(daccout_provider):
    print(daccout_provider)

#带参数的fixture，写法二
@pytest.mark.parametrize("account_provider",[{'username':'test1','password':'1'},
                        {'username':'test2','password':'2'}])
def test_login(account_provider):
    print(account_provider)

'''
#直接写函数读取外部文件生成数据值，注意values返回值是个list
my_file = '/Users/yuanyuan/PycharmProjects/126logincase.csv'
data = csv.reader(open(my_file, 'r', encoding='gbk'))
@pytest.mark.parametrize('loginfo',data)
def test_login(loginfo):
    print(loginfo)
'''
#fixture是封装在类的前面声明
@pytest.fixture()
def before():
    print('\nbefore each test')

@pytest.mark.usefixtures("before")
class Test2:
    def test_5(self):
        print('test_1()')

    def test_6(self):
        print('test_2()')
'''


'''
#可以看到mod_header在该module内运行了一次，而func_header对于每个test都运行了一次，总共两次。
@pytest.fixture(scope="module", autouse=True)
def mod_header(request):
    print('\n-----------------')
    print('module      : %s' % request.module.__name__)
    print('-----------------')

@pytest.fixture(scope="function", autouse=False)
def func_header(request):
    print('\n-----------------')
    print('function    : %s' % request.function.__name__)
    print('time        : %s' % time.asctime())
    print('-----------------')

def test_one():
     print('in test_one()')

def test_two():
    print('in test_two()')
'''
