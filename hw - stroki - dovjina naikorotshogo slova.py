def dov(n):
    min1=len(n)
    min=()
    s=n.split()
    for i in s:
        if len(i)>min1:
            min=i
    return min
print(dov(input()))