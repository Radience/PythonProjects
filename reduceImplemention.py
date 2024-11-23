def reduce(func, seq):
    value = 0
    for x in iter(seq):
        value = func(value, x)
    return value

seq = [1,2,3]
print("sum seq is:", reduce(lambda x,y: x + y, seq))
