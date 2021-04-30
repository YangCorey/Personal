#https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/
from typing import List
class Solution:
    def __init__(self):
        self.history = set() 
        self.result = set()

    def tot_sign(self, ind):
        tot = sum([self.nums[i] for i in ind])
        if tot == 0:
            sign = 0
        else:
            sign = -1 if tot < 0 else 1
        return tot,sign 

    def threeSumHelp(self, l, m, u, dir_check):

        print(l,m,u, dir_check)
        if (l+1) >= u or (l,u)in self.history or self.nums[l] > 0 or self.nums[u] < 0:
            return [] 
        self.history.add((l,u))

        res = []
        if m is not None:
            low = m if dir_check else m
            upper = u if dir_check else l
            step = 1 if dir_check else -1
        else:
            low = l+1
            upper = u
            step = 1
        tot,sign = self.tot_sign([l,u])
        if tot == 0 :
            _,sign = self.tot_sign([l,u,low])

        zero_check = True

        print("range",low,upper,step)
        for i in range(low,upper,step):
            ind = [l,i,u]
            print("ind",ind)
            tot_temp,sign_temp = self.tot_sign(ind)

            if tot_temp == 0:
                print("add",ind)
                self.result.add((self.nums[l],self.nums[i],self.nums[u]))
                zero_check = False
                break
            elif sign_temp != sign:
                print("sign change", ind)
                zero_check = False
                break
            low += step 
        
        if zero_check:
            print("zero_check:True")
            self.threeSumHelp(l,None,u-1,None) if sign>0 else self.threeSumHelp(l+1,None,u,None)
        else:
            print("zero_check:False")
            self.threeSumHelp(l,low,u-1,True) + self.threeSumHelp(l+1,low,u,False)
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.history = set()
        nums.sort()
        self.nums = nums
        print(nums)
        l = 0
        u = len(self.nums) - 1
        res = []
        self.threeSumHelp(l,None,u,None)
        return [list(x) for x in self.result]

sol = Solution()
#print(sol.threeSum(nums = [-2,0,1,1,2]))
#print(sol.threeSum(nums = [-1,0,1,2,-1,-4]))
#print(sol.threeSum(nums = [0,0,0]))
print(sol.threeSum(nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]))
#print(sol.threeSum(nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
print([ (i,val) for i,val in enumerate(sol.nums)])
