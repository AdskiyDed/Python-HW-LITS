class Stek:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dod(self):
        if len(self.x)!=0:
            for i in range (len(self.y)):
                (self.x).append(self.y[i])
            return self.x, len(self.x)
        else:
            print ('pustoi')
            # exit
    def delit(self):
        if len(self.x) != 0:
            return (self.x).pop(), len(self.x)
        else:
            print ('pustoi')
            exit
z = Stek([6, 8, 10, 1],[2,3])
print(z.dod())
print(z.delit())
