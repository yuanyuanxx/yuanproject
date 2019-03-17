from collections import namedtuple
import pytest
import time

#构建一个可命名的元祖
Task=namedtuple( 'Task' , ['summary' ,  'owner' ,  'done' ,  'id' ])
Task.__new__.__defaults__ = (None, None, False, None)

def  test_defaults():
 """不使用参数应调用默认值"""
t1 = Task()
t2 = Task(None, None, False, None)
assert  t1 == t2


def  test_member_access():
 """检查namedtuple的.field功能"""
 t = Task('buy milk' ,  'brian' )
 assert  t.summary == 'buy milk'
 assert  t.owner == 'brian'
 assert  (t.done, t.id) == (False, None)

def test_asdict():
     """_asdict() 将对象转换成字典"""
     t_task = Task('do something', 'okken', True, 21)
     t_dict = t_task._asdict()
     expected = {'summary': 'do something','owner': 'okken','done': True,'id': 21}
     assert t_dict == expected

@pytest.mark.run
def test_replace():
    """replace() 修改对象属性."""
    t_before = Task(' finish book', 'brian', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task(' finish book', 'brian', True, 10)
    assert t_after == t_expected

@pytest.mark.run_these
def test_member():
    a=[1,2]
    b=[1,2]
    time.sleep(3)
    assert a==b
