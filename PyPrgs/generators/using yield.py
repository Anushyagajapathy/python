a="anushya"
b=iter(a)
while True:
    try:
        c=next(b)
        print(c)
    except StopIteration:
        print("error")
        break
    


