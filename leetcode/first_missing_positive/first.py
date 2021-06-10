from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            val = nums[i] - 1
            if i == val:
                i += 1
                continue
            if 0 <= val and val < len(nums) and (nums[val]-1) != val:
                nums[i], nums[val] = nums[val], nums[i]
            else:
                i +=1
        res = 1
        i = 0
        while i < len(nums):
            if res != nums[i]:
                return res
            res += 1
            i += 1
        return res
sol = Solution()
print(sol.firstMissingPositive([4,3,1,2,7,8,5,10]))
