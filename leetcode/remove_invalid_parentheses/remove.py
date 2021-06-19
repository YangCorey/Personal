from typing import List
class Solution:
    def string_poss(self, ind, rem_ct , total_ct, s, target):
        print(ind, rem_ct, total_ct, s, target)
        res = set()
        if rem_ct == 0:
            res.add(s)
            return res
        #If we have reached end of string or are trying to remove more than the remaining existing
        if ind >= len(s) or rem_ct > total_ct:
            return res

        if s[ind] == target:
            total_ct -= 1
            res = res | self.string_poss(ind, rem_ct - 1, total_ct, s[0:ind] + s[ind+1:len(s)], target)
        res = res | self.string_poss(ind + 1, rem_ct, total_ct, s, target)
        return res





    def removeInvalidParentheses(self, s: str) -> List[str]:
        print(s)
        #Store the close_ind, closing_ct and number of which ")" outnumber "(" 0 to len(s) 
        #Store the open_ind, open_ct, and number of which "(" outnumber ")" going from len(s) to open_ind 
        #Pass both to recursive methods that will check every combination of keeping or removing parenthesis
        i = 0
        while i < len(s) and s[i] == ")":
            i += 1
        s = s[i:]
        i = len(s) - 1 
        while 0 < i and s[i] == "(":
            i -= 1
        s = s[:i+1]

        close_ind = - 1 
        close_over = 0

        close_open_ct = 0

        for i in range(len(s)):
            if s[i] == "(":
                close_open_ct += 1
            elif s[i] == ")":
                close_open_ct -= 1
                if close_open_ct < close_over:
                    close_over -= 1
                    close_ind = i
        close_over *= -1
        close_ct = sum([ 1 for char in s[0:close_ind+1] if char == ")" ])

        left_poss = self.string_poss(ind = 0, rem_ct = close_over , total_ct = close_ct, s = s[0:close_ind + 1], target = ")") if close_over != 0 else set([""])

        open_ind =len(s) 
        open_over = 0
        close_open_ct = 0

        while i > close_ind:
            if s[i] == "(":
                close_open_ct += 1
                if close_open_ct > open_over:
                    open_over += 1
                    open_ind = i
            elif s[i] == ")":
                close_open_ct -= 1
            i -= 1

        open_ct = sum([ 1 for char in s[open_ind:] if char == "(" ])
        right_poss = self.string_poss(ind = 0, rem_ct = open_over , total_ct = open_ct, s = s[open_ind:], target = "(") if open_over != 0 else set([""])

        res = []
        for left in left_poss:
            for right in right_poss:
                res.append(left+s[close_ind+1:open_ind]+right)
        return res

sol = Solution()
print(sol.removeInvalidParentheses("(a)())()()(()()"))
print(sol.removeInvalidParentheses("(r(()()"))
print(sol.removeInvalidParentheses("()())()"))
print(sol.removeInvalidParentheses("(((()(()"))
