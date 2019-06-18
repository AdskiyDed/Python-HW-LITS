def star_print(f):
    def inner():
        print('************')
        f()
    return inner
@star_print
def f():
    print("Hi")
f()