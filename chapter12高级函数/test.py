# 匿名函数
"""
def add(x,y):
    return x+y

# lambda 表达式
f = lambda x,y : x+y

f(11,3)
"""

# 三元表达式 非python
# x > y ? x : y
# python 三元表达式
# f = x if x > y else y

# 函数式编程(二)
list_x = [1,2,3,4,5,6]

def f(x):
    return x * x

# for x in list_x:
#   f(x)

r = map(f, list_x) # map 映射
rr = map(lambda x:x*x, list_x) 
print(list(r))