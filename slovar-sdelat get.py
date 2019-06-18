#зробити функцію get для словаря
# d={1:11,2:22,3:33}
# def get(d,k,v=None):
#     if k in d:
#         return d[k]
# print(get(d,2))

# поєднати два словаря, якщ є спільні ключі, то їх значення сумувати
# varian 1
# d={1:'m',2:22,3:33,4:44}
# d1={1:'n',4:9,5:33,6:33}
# def get(d,d1,v=None):
#     s=set()
#     for i in d.keys():
#         s.add(i)
#     s1 = set()
#     for i in d1.keys():
#         s1.add(i)
#     n=tuple(s.intersection(s1))
#     for i in n:
#         d1[i]=d[i]+d1[i]
#     d.update(d1)
#     return d
# print(get(d,d1))

#variant 2
d={1:'m',2:22,3:33,4:44}
d1={1:'n',4:9,5:33,6:33}
def get(d,d1,v=None):
    for key in d:
        for key1 in d1:
            if key==key1:
                d1[key]=d[key]+d1[key]
    d.update(d1)
    return d
print(get(d,d1))