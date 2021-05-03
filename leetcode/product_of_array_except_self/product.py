from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        total_l = 1
        total_r = 1
        for i in range(len(nums)):
            r_i = len(nums)-1-i
            res[i] = res[i] * total_l
            total_l *= nums[i]

            res[r_i] = res[r_i]*total_r
            total_r *= nums[r_i]
        return res
sol = Solution()
print(sol.productExceptSelf(nums = [1,2,3,4]))
