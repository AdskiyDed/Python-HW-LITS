def dov(n):
    min=len(n)
    s=n.split()
    for i in s:
        if min>len(i):
            min=len(i)
    return min
print(dov(input()))