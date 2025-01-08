l1 = [2,4,9]
l2 = [5,6,4,9]
def addTwoNumbers(l1, l2):
    ans = list(reversed(list(map(str, str(int(''.join(map(str, l1))) + int(''.join(map(str, l2))))))))
    return(ans)

print(addTwoNumbers(l1, l2))
