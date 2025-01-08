listInput = ["hello", "new", "world"]

def calcGematry(word):
    num = 0
    for char in iter(word.upper()):
        num += (ord(char) - ord('A'))
    return num

def sortGematry(lst):
    dictOut = {}
    for x in iter(lst):
        dictOut[f"{x}"] = int(calcGematry(x))
    print(list(sorted(dictOut.items(), key=lambda item: item[1])))

sortGematry(listInput)
