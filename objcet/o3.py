# 成员私有性和公开性
from o4 import Human


class Student(Human):

    # name = ''
    # age = 0
    # sum = 0
    # # __score = 0
    def __init__(self, school, name, age):
        self.school = school
        super(Student,self).__init__(name,age)
    # 变量或方法前加双下划线，将其变为私有

    def do_homework(self):
        print('english homework')

    def marking(self, score):
        if score < 0:
            return '不可以打负分'
        self.__score = score
        print(self.name + ' 本次考试的分数是：' + str(self.__score))


student1 = Student('Chongnam', 'jack', 17)
student1.get_name()
print(student1.sum)
