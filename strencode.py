#coding=utf8

# 测试pyhton 2.7 下 utf-8 

#from __future__ import print_function, unicode_literals
from __future__ import  unicode_literals
import requests
import re
import sys
import codecs
#import win32console

def cp65001(name):
    if name.lower() == 'cp65001':
        return codecs.lookup('utf-8')
    
#codecs.register(cp65001)

reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
#sys.stderr = codecs.getwriter('utf8')(sys.stderr)
#import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)


checkstr = '密码不正确'
utf8=checkstr.encode(encoding='utf8')

for i in utf8:
    print ord(i)

for i in checkstr:
    print ord(i)


for i in utf8.decode(encoding='utf8'):
    print ord(i)    

#print utf8
