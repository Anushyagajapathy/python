D= {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
d = {k: ('old' if v > 40 else 'young') for (k, v) in D.items()}
print(d)
