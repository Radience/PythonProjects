res = ""
        print(len(strs))
        for x in range(len(min(strs, key=len))):
            res += strs[strs.index(min(strs, key=len))][x]
            for y in range(len(strs)):
                print(
                    f"--------\ncircle:{y}\nresult:[{res}]\nword:{strs[y]}\nchar:{strs[y][x]}"
                )
                if strs[y][x] != res[x]:
                    res = res.replace(res[len(res) - 1], "")
                    return res
        return res
