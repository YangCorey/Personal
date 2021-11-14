class Solution:
    def comb(self,candidates, target):
        print(candidates,target)
        if target in self.hist:
            return self.hist[target]
        self.hist[target] = []
        for candidate in candidates:
            div = target//candidate
            for mul in range(div + 1):
                print(candidate,mul)
                if candidate*div == target:
                    self.hist[target].append([candidate]*div)
                else:
                    next_tar = self.comb(candidates, target - (mul*candidate))
                    print("1",next_tar)
                    for next_temp in next_tar:
                        print("2",next_temp)
                        self.hist[target].append([candidate]*mul + next_temp)
        return self.hist[target]

        
    def combinationSum(self, candidates, target: int):
        self.hist = {0:[]}
        return self.comb( candidates, target)
    
sol = Solution()
res = sol.combinationSum(candidates = [2,7,6,3,5,1], target = 9)
print(res)
