import math

from palyLA._global import EPSILON


class Vector:
    def __init__(self,lst):
        self._values = list(lst)
    def __len__(self):
        return len(self._values)
    def __getitem__(self, index):
        return self._values[index]
    def __repr__(self):
        return "Vector({})".format(self._values)
    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))
    def __add__(self, another):
        assert len(self) == len(another),\
            "Error in adding. Length of vectors must be same."
        return Vector([a + b for a, b in zip(self,another)])
    def __iter__(self):
        return self._values.__iter__()
    def __sub__(self, another):
        assert len(self) == len(another), \
            "Error in adding. Length of vectors must be same."
        return Vector([a - b for a, b in zip(self, another)])
    def __mul__(self, k):
        return Vector([k * a for a in self])
    def __rmul__(self, k):
        #return Vector([k * a for a in self])
        return self * k
    def __pos__(self):
        return 1 * self
    def __neg__(self):
        return -1 * self
    # 类方法 对象方法.
    @classmethod
    def zero(cls,dim):
        return cls([0] * dim)
    # todo 向量的模 归一化 规范化(normalize) 标准单位向量 Standard Unit Vector
    def norm(self):
        return math.sqrt(sum(e ** 2 for e in self._values))
    def normlize(self):
        #return Vector([e / self.norm for e in self._values])
        if self.norm() < EPSILON:
            raise ZeroDivisionError("Normlize error! norm is zero")
        return Vector(self._values) / self.norm()
    def __truediv__(self, k):
        """返回数量除法的结果向量: self / k"""
        return (1 / k) * self
    def  dot(self,another):
        """向量点乘 结果标量"""
        # 向量点乘的应用 判断两个向量的相似程度(推荐系统)
        assert len(self) == len(another), \
            "Error in adding. Length of vectors must be same."
        return sum( a * b for a,b in zip(self,another))
