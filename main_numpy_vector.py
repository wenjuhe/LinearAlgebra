import numpy as np
if __name__ == "__main__":
    print(np.__version__)
    lst = [2,3,4]
    lst[0] = 'Linear Algebra'
    print(lst)
    vec = np.array([1,2,3])
    print(vec)
    # vec[0] = 'Linear Algebra'
    vec[0] = 666
    print(vec)
    # np.array的创建
    print(np.zeros(5)) #浮点型
    print(np.ones(5))
    print(np.full(5,666))
    # np.array的基本属性
    print("size = ", vec.size)
    print("size = ", len(vec))
    print(vec[0])
    print(vec[-1])
    print(vec[0:2]) # 切片
    print(type(vec[0:2]))
    # np.array的基本运算
    vec2 = np.array([4,5,6])
    print("{} + {} = {}".format(vec,vec2,vec+vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))
    print("{} * {} = {}".format(2, vec2, 2 * vec2))
    print("{} * {} = {}".format(vec, vec2, vec * vec2)) # 逐个元素的乘法
    print("{}.dot({}) = {}".format(vec, vec2, vec.dot(vec2))) # 逐个元素的乘法
    print(np.linalg.norm(vec))
    print(vec / np.linalg.norm(vec))
    print(np.linalg.norm(vec / np.linalg.norm(vec)))
    zero3 = np.zeros(3)
    zero3 / np.linalg.norm(zero3)