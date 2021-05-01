#https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/
from typing import List
class Solution:
    def __init__(self):
        self.history = set() 
        self.result = set()

    def threeSumHelp(self, const, l):
        target = -1*self.nums[const]

        if target in self.history:
            return []
        self.history.add(target)

        temp_hist = set() 
        res = []
        h = len(self.nums)-1
        while l < h:
            temp_sum = self.nums[l] + self.nums[h]
            if temp_sum == target:
                if [self.nums[const], self.nums[l], self.nums[h]] not in res:
                    res += [[self.nums[const], self.nums[l], self.nums[h]]]
                l += 1
                h -= 1
            elif temp_sum < target:
                l += 1
            else:
                h -= 1
        return res


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.history = set()
        nums.sort()
        self.nums = nums
        res = []
        for i in range(len(nums)-2):
            res += self.threeSumHelp(i, i+1)

        return res
sol = Solution()
#print(sol.threeSum(nums = [-2,0,1,1,2]))
#print(sol.threeSum(nums = [-1,0,1,2,-1,-4]))
#print(sol.threeSum(nums = [0,0,0]))
#print(sol.threeSum(nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]))
#print(sol.threeSum(nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
#test asd
print(sol.threeSum(nums = [-2,0,0,2,2]))

print([ (i,val) for i,val in enumerate(sol.nums)])

