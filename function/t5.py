# 参数
# 1. 必须参数
# 2. 关键字参数 add(y = 1, x = 2) 不用考虑顺序
#    代码可读性
# 3. 默认参数
#    默认参数必须放在最后面
# 关键字参数 默认参数 顺序不能混乱


def print_student_files(name, gender='boy', age=18, college='qinghua'):
    print('My name is ' + name)
    print('I\'m ' + str(age) + ' years old')
    print('I am ' + gender)
    print('My college is ' + college)


print_student_files('Peter')
print_student_files('Mike')
