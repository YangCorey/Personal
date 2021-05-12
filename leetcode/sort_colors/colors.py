from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        pos = {0:None , 1:None, 2:None }

        for i,val in enumerate(nums):
            if pos[val] is None:
                pos[val] = i
            for j in range(val+1,3):
                if pos[j] is not None and i > pos[j]:
                    print("i:",i,"j",pos[j])
                    nums[i], nums[pos[j]] = nums[pos[j]], nums[i]
                    if pos[j] < pos[val]:
                        pos[val] = pos[j]
                    pos[j] += 1


sol = Solution()
nums = [2,0,2,1,1,0,2,2,2,1,0,1,2,0,1]
sol.sortColors(nums )
print(nums)
