@staticmethod
def funcname(parameter_list):
    pass

# 1. 参数列表可以为空
# 2. return value 如果没有则认为返回为None


def add(x, y):
    result = x + y
    return result


def print_code(code):
    print(code)


add(1, 2)
print_code(add(1, 2))
