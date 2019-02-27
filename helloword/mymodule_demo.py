
def say_hi():
    print('HI,this is mymodule speaking.')
__version__='0.1'

say_hi()
print(__version__)

#使用import
import mymode

mymode.say_hi()
print('Version',mymode.__version__)

'''
from mymode import say_hi,__version__

say_hi()
print('Version',__version__)
'''
