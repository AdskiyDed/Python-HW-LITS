def counter(f):
    count=0
    def inner (*arg,**kw):
        nonlocal count
        count+=1
        f(*arg,**kw)
        inner.count=count
    return inner
@counter
def p():
    print('Hi')
p()
p()
p()
print(p.count)
