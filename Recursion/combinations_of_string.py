def combinations(s):

    def dfs(temp, idx):
        if temp != []:
            print("".join(temp))
        for i in range(idx, len(s)):
            temp.append(s[i])
            # backtrack
            dfs(temp, i + 1)
            temp.pop()

    dfs([], 0)

s = "abc"
combinations(s)