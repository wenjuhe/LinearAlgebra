from palyLA.Vector import Vector
if __name__ == "__main__":
    vec = Vector([5,2])
    print(vec)
    print(len(vec))
    print("vac[0] = {},vec[1] = {}".format(vec[0],vec[1]))
    vec2 = Vector([3,1])
    print("{} + {} = {}".format(vec,vec2,vec + vec2))
    print("{} - {} = {}".format(vec,vec2,vec - vec2))
    print("{} * {} = {}".format(vec,7,vec * 7))
    print("{} * {} = {}".format(7,vec,7 * vec))
    print("+{} = {}".format(vec,+vec))
    print("-{} = {}".format(vec,-vec))

    zero2 = Vector.zero(2)
    print(zero2)
    zero3 = Vector.zero(3)
    print(zero3)
    print("norm({}) = {}".format(vec,vec.norm()))
    print("norm({}) = {}".format(zero2,zero2.norm()))
    print("normlize {} is {}".format(vec,vec.normlize()))
    print(vec.normlize().norm())
    try:
        print(zero2.normlize())
    except ZeroDivisionError:
        print("Cannot normlize zero vector {}".format(zero2))
    print(vec.dot(vec2))