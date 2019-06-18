def power(a, n):
    if n==0:
        return 1
    else:
        return a*power(a,n-1)
    return res
print(power(float(input()), int(input())))
