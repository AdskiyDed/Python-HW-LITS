def mul2(func):
    def inner(*arg):
        r=func(*arg)
        return 2*r
    return inner
@mul2
def f(a,b):
    return a*b
print (f(4,3))