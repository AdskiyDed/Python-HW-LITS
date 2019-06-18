def smart_input():
    s=input()
    d=s.split(' ')
    max=0
    for i in d:
        i=int(i)
        if i>max:
            max=i
    return(max)
print(smart_input())
