from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        print(nums)
        prev, max_val = nums[0], nums[0]
        first_neg = None if nums[0] >= 0 else nums[0]
        for i in range(1, len(nums)):
            if prev == 0 :
                first_neg = None
                prev = 1
            prev *= nums[i]
            curr_max = max(prev,nums[i]) if first_neg is None or prev > 0 else max(prev,nums[i],prev//first_neg)
            if prev < 0 and first_neg is None:
                first_neg = prev

            print("i",i,"prev",prev, "first_neg",first_neg, "max", max_val,"curr_max", curr_max)
            if curr_max > max_val:
                max_val = curr_max
        
        return max_val
sol = Solution()

print(sol.maxProduct(nums = [-1,-2,-3,0]))
print(sol.maxProduct(nums = [2,-1,-2,-5,0, 3,-2,-3,-10]))

