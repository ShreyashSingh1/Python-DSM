def test():
    return 1, 3, 3, "we", 34

a, b, c, d, e = test()
print(a, b, c, d, e)


def test1():
    """Separates the int """
    l = [11, 3, 45, 5, 6, 7, "Shreyash", "Singh", [1, 2, 3, 4]]
    l1_num = []
    for i in l:
        if type(i) == int or type(i) == float:
            l1_num.append(i)

        if type(i) == list:
            for j in i:
                if type(j) == int or type(j) == float:
                    l1_num.append(j)

    return l1_num

print(test1())


# Unlimited Position arguments
def test2(*args):
    """It Stores in form of tuples"""
    return args

print(test2(1, 3, 3, 3, 3))

def test3(**kwargs):
    """It stores in format of dictionary"""
    return kwargs

print(test3(a=[2, 4, 4, 3], b="Shreyash"))





