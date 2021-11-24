import time
start=time.time()
def topten():
    yield 5
a=topten()
print(next(a))
end=time.time()
print("Time:",end-start)
