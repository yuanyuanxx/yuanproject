import pytest

a=[2,5,4]
def  test_main():
    assert 4 in a

#运行模块中，测试类里面的某个方法  pytest  basic\ exercise/test_txt02.py::test_sum
#pycharm -termianl :pytest -v basic\ exercise/test_txt02.py

#终端命令：yuanyuanzhoudeMacBook-Pro:basic exercise yuanyuan$ pytest -v test_txt01.py::test_demo1
#当前目录下执行用例并生成报告hj,：basic exercise yuanyuan$ pytest --html=report.html --self-contained-html

if __name__=='__miakn__':
    #制定某个测试文件
    pytest.main("pytest exe01/")
    #指定测试目录
    #pytest.main("/users/yuanyuan/PycharmProjects/pytest/exe01")k
