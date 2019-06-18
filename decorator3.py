def is_b_zero(f):
    def inner(a,b):
        if b==0:
            print('b==0')
        else:
            c=f(a,b)
            return c
    return inner
@is_b_zero
def f(a,b):
    print(a/b)
f(int(input()),int(input()))