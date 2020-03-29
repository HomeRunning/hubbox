from functools import reduce


# 连续计算,连续调用lambda表达式
# 第一次调用前两个list元素,第一次结果与第二个元素继续计算,以此类推
# list_x = [1,2,3,4,5,6]
# r = reduce(lambda x,y: x+y, list_x,初始值选填) 

list_xy = [(1,2),(1,0),(2,0),(3,6)]
r = reduce(lambda x,y:x+y,list_xy)
print(r)