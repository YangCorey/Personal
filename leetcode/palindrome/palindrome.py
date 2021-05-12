from typing import List
class Solution:
    def partition_help(self, s, start, end):
        res = [[]]
        pal_check = False 
        if start > end:
            return [[]], True 
        if (start,end) in self.history:
            return [[]], self.history[(start,end)]
        if start == end:
            self.history[(start,end)] = True
            return [[s[start]]], True
        

        if s[start] == s[end]: 
            res_inner, prev_pal = self.partition_help(s,start+1,end-1)
            if prev_pal:
                res.append([s[start:end+1]])
                pal_check = True
        left_res, _ = self.partition_help(s,start, end-1)
        right_res, _ = self.partition_help(s,start+1, end)
        print(s,start,end)
        print("left", left_res)
        print("right", right_res)

        for left_temp in left_res:
            for right_temp in right_res:
                res.append(left_temp + right_temp)
        self.history[(start,end)] = pal_check

        return res, pal_check

    def partition(self, s: str) -> List[List[str]]:
        self.history = {}
        return self.partition_help(s,0, len(s)-1)[0]

sol = Solution()
print(sol.partition("aab"))
#print(sol.partition("aabb"))
