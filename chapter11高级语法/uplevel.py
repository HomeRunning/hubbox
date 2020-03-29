# 函数式编程

# 1. 闭包 函数内定义环境变量 不外部影响(需要引用环境变量)
# 闭包保存一个环境(现场)

def curve_pre():
    a = 4
    b = 3
    def curve(x):
        y = a*x*x + b*x 
        return y
    return curve

#f = curve_pre()

#print(f(3))

# global关键字 全局定义 
x_scale = 0
def travel(x_scale):
    def move(x):
        newx = x_scale + x
        x_scale = newx
        return x_scale
    return move

f = travel()
print(f(2))
print(f(3))
print(f(2))
