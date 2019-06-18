class Square:
    def __init__(self,a, b):
        self.a = a
        self.b = b
    @staticmethod
    def S( a, b):
        return (a+b)*2
    @staticmethod
    def K(a,b):
        return a*b
    @property
    def s(self):
        return Square.K(self.a, self.b)
m = Square(5,6)
print(m.S(5,7))
print(m.K(4,8))
print(m.s)

# def singletone (cls): #decorator dlia class
#     instance=None
#     def inner(*args,**kw):
#         nonlocal instance
#         if instance is None:
#             instance=cls(*args,**kw)
#         return instance
#     return inner
# @singletone
# class Point:
#     def __init__(self,x, y):
#         self.x = x
#         self.y = y
# p1=Point(4,5)
# p2=Point(3,4)
# print(p1 is p2)

