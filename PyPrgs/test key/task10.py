def sale():
    n = [{'country':'india','sale':150.2},
    {'country':'china','sale':250.2},
    {'country':'malasia','sale':149},
    {'country':'America','sale':130.9}]
    s=list(map(lambda n: n['sale'],n))
    return s
