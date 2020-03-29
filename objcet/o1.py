# 面向对象
# 有意义的面向对象代码
# 类 = 面向对象 X
# 实例化
# 类最基本作用是封装代码


class Student():
    sum_s = 0
    name = ''
    age = 0
# 类变量， 实例变量
    # 构造函数

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('student')

    # 实例方法 self可变 必需 代表对象本身

    def print_file(self):
        print('name' + self.name)
        print('age' + str(self.age))
    
    # 类方法的定义
    # cls可变，代表类本身
    # 实例也可以调用类方法 不推荐
    @classmethod
    def plus_sum(cls):
        cls.sum_s += 1
        print(cls.sum_s)

    # 静态方法 
    # 可被类或实例对象调用
    @staticmethod
    def add(x, y):
        print('this is a static method')

# 方法和函数的区别
# 方法：设计层面 函数：程序运行、过程
# student = Student() 
# student.print_file()


student1 = Student('Jack', 18)
Student.plus_sum
print(student1.name)
print(student1.__dict__)
print(Student.__dict__)
