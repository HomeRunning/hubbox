# 装饰器
import time

def decorator(func):
    def wraaper(*args,**kw):
        print(time.time())
        func(*args,**kw)
    return wraaper

@decorator
def f1(name):
    print("begin time: "+name)

@decorator
def f2(name1, name2):
    print(name1+" and "+name2)

@decorator
def f3(name1,name2,**kw):
    print(name1+" and one "+name2)
    print(name1+" and two "+name2)
    print(name1+" and three "+name2)
    print(kw)


f1("tom")
f2('tmo','jerry')
f3('tom','jerry', a=1,b=2,c='123')
# @
# f = decorator(f1)
# f()
