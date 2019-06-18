s=set([1,2,3])
s1=set([3,4,5])
def sp(s,s1):
    s=set(s)
    s1=set(s1)
    s.intersection(s1)
    return s.intersection(s1)
print(sp(s,s1))