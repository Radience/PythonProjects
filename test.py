s = "a"
PosChars = []
ListWithoutDuplicate = []
MaxOdds = []
if s.isalpha() or " " in s:
    [ListWithoutDuplicate.append(y) for y in s if y not in ListWithoutDuplicate]
    [PosChars.append([pos+1 for pos, char in enumerate(s) if char == x]) for x in ListWithoutDuplicate]
    [MaxOdds.append(PosChars[x][y+1] - PosChars[x][y]) for x in range(len(PosChars)) for y in range(len(PosChars[x])) if len(PosChars[x]) > 1 and y < int(len(PosChars[x])-1)]
    print(PosChars)
    print(ListWithoutDuplicate)
    print(max(MaxOdds))
