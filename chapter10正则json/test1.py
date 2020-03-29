import re

a = 'C0C++7Java8C#Python96panda5'#(普通字符)

r = re.findall('\d',a) # \d表示数字(元字符)
print(r)

s = 'acb, abd, aed, aod, afb'

r_1 = re.findall('a[cf]b',s) # ^a[cf]b中 ^表示取反 []或 ()且
print(r_1)

# 数量词[a-z]{1,9} 表示规则下匹配的数量范围 
# 贪婪 与 非贪婪 默认贪婪模式, 加?是贪婪模式
 
p = 'nding333j'

r_2 = re.findall('333$',p)
print(r_2)

# *********************************************************
r_3 = re.sub('3', '2', 0) # 替换 第二个参数传入函数           *
def fun(value):  # 第一个参数传入value 但是value是一个对象     *
    pass         #                                        *
# *********************************************************