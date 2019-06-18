class Rom(int):

    def __init__(self, data,s=10):
        self.data = data
        self.s = s
        self.d = int(self.data, self.s)

    def checkio(self):

        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thous = ["", "M", "MM", "MMM", "MMMM"]

        t = thous[self.d // 1000]
        h = hunds[self.d // 100 % 10]
        te = tens[self.d // 10 % 10]
        o = ones[self.d % 10]
        rim = t + h + te + o
        return rim

    def __add__(self, other):
        return Rom(str(self.d+other))

    # def __sub__(self, other):
    #     return self.d-other
    #
    # def __mul__(self, other):
    #     return self.d*other
    #
    # def __eq__(self, other):
    #     return self.d == other

z=Rom('10111',2)
z1=Rom('065',8)
print(z.checkio(),z1.checkio())
print(z+z1)
# print(z-z1)
# print(z*z1)
# print(z==z1)


