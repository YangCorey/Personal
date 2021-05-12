from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = {} 
        res_history = {}
        check = {}

        for i in range(len(s))[::-1]:
            res[i] = []
            res_history[i] = []

            for j in range(i, len(s)):
                if s[i] == s[j] :
                    if j <= i+1 or (i+1 in res_history and j-1 in res_history[i+1] ):
                        res_history[i].append(j)
                        if j + 1 in res:
                            for res_temp in res[j+1]:
                                res[i].append([s[i:j+1]] + res_temp)
                        else:
                            res[i].append([s[i:j+1]])
        return res[0]

sol = Solution()
print(sol.partition("aabaa"))
x = [["a"]]
x.append(["asd"] +["a"])
print(x)
