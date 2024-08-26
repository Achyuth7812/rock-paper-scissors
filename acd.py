'''from functools import reduce


nlist=[1,2,5,78]
def maxi(x,y):
    if x>y:
        return x
    else:
        return y
print(reduce(maxi,nlist))     '''
def outer():
    x = 10 #local
    print("within outer x:",x)
    def inner():
        nonlocal x
        x = 20 #x from outer funtion
        print("within inner x:",x)
    inner()
x = 5 #global
print("Before outerx:",x)
outer()
print("After outer x:",x)