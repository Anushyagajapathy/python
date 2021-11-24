from functools import reduce
def max():
    n = [100,10,20,200,30,40,50]
    s=reduce(lambda x,y: x if x>y else y,n)
    return s
