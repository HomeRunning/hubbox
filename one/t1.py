# Python项目的组织结构
# 包 模块 类<函数、变量
# 物理表示 文件夹为包，py文件为模块 class为类
# 表示同名文件
# one.t1
# two.t1
# 命名空间

# 导入的两种方式
import one.t1
from one.t1 import a
# 如果导入模块中有大量变量或函数用*可一次性导入，不推荐
# 也可以用 逗号 分隔，选择导入
from one.t1 import *
# 包和模块是不会被重复导入
