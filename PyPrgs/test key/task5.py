from functools import reduce
def addusingreduce():
    n = [10,20,30,40,50]
    s= reduce(lambda x,y:x+y,n)
    return s
