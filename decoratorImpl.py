def even_check(func):
    def check(*args):
        num = func(*args)
        if num % 2 == 0:
            print("even:", num)
        else:
            print("odd:", num)
    return check

@even_check
def SummaryNumber(*_property):
    num = 0
    for x in _property:
        num += x
    return num

print(SummaryNumber(1, 1, 1, 1))
