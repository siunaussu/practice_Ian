def dec(func):
    def w(*args,**kwargs):
        print(args, kwargs)
        return func(*args,**kwargs)
    return w

@dec
def f(a,b,c=10):
    print("YDC")
    return a+b+c

res = f(1,2,c=100)
print(res)