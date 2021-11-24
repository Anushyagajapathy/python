def deletevalue():
    s = ['india','usa','uk','france','germany']
    n = list(filter(lambda x:len(x)>3,s))
    return n
