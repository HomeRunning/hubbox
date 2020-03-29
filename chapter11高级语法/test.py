# 枚举
from enum import Enum
from enum import IntEnum,unique #IntEnum 强制int型枚举, unique装饰器,不允许枚举有相同值

#属于单例模式
#设计模式对修改关闭,对扩展开放
@unique
class VIP(Enum):
    """继承枚举类"""
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

print(VIP.YELLOW)