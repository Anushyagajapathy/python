
n = [{'country':'india','sale':150.2},
{'country':'china','sale':250.2},
{'country':'malasia','sale':149},
{'country':'America','sale':130.9}]
s=list(filter(lambda x:x["sale"]>200,n))
print(s)
