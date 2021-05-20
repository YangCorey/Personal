from typing import List
import statistics
import random 
class Solution:
    def kSmallest(self, pos, nums):
        pivot = random.randint(len(nums))
        pivot_val = nums.pop(pivot)
        i,j = 0, len(nums)-1

        while i < j:
            if nums[i] < pivot_val:
                i += 1
            elif nums[i] > pivot_val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1


        if nums[i] < pivot_val:
            i += 1

        if i == pos:
            return pivot_val
        elif i > pos:
            return kSmallest(pos-(i+1), nums[:i])
        else:
            return kSmallest(pos,nums[i:])



    def wiggleSort(self, nums: List[int]) -> None:
        avg = statistics.median(nums)
        
        i,j,k = 0,0,len(nums)-1

        while j <= k:
            if nums[j] > avg:
                nums[i],nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] < avg:
                nums[j],nums[k] = nums[k], nums[j]
                k -= 1
            else:
                j += 1

        i, j, k = 0, 0, len(nums)-1
        n = len(nums) 
        func = lambda i: (2*i+1)%(n|1)

        while j<=k:
            if nums[func(j)] > avg:
                nums[func(j)], nums[func(i)] = nums[func(i)], nums[func(j)]
                i += 1
                j += 1
            elif nums[func(j)] < avg:
                nums[func(j)], nums[func(k)] = nums[func(k)], nums[func(j)]
                k -= 1
            else:
                j += 1


nums = [2,2,2]




nums = [4,4,4,2,2,5]



nums = [1,5,1,1,6,4]




nums = [5,5,5,4,4,4,4]


nums = [1,4,3,4,1,2,1,3,1,3,2,3,3]

nums = [1,3,2,2,3,1]

nums = [5,3,1,2,6,7,8,5,5]
nums = [4,5,5,6]

nums = [3,6,6,7,2,9,10,8,8,10,3,4,7,8,9,5,6,8,8,4,7,3,7,7,5,10,4,2,8,9,5,1,8,4,8,10,6,5,5,9,6,5,2,1,4,3,9,1,3,7,6,4,4,9,1,5,3,5,1,10,1,10,10,6,5,9,10,8,1,1,10,4,1,4,4,2,7,6,2,2,1,9,7,9,9,5,5,10,2,9,3,3,9,6,2,4,6,10,1,2,6,1,2,2,7,7,1,4,7,3,4,7,1,7,7,10,9,8,3,2,5,3,6,9,9,7,4,4,4,6,7,3,9,6,2,1,9,3,3,2,1,4,8,3,5,3,4,5,2,6,6,3,9,8,8,7,4,7,5,3,6,5,1,5,10,1,1,9,10,10,9,1,2,9,5,10,4,2,5,2,4,10,6,1,4,5,1,1,2,4,2,1,6,1,10,8,9,6,8,7,6,8,7,4,6,10,2,8,5,4,4,1,2,8,9,8,4,10,8,1,3,5,1,6,7,9,8,6,4,2,3,8,4,4,8,10,7,10,8,10,8,10,7,3,6,9,9,9,10,8,3,8,1,3,5,5,8,5,5,7,6,3,1,9,9,6,3,7,1,7,4,7,2,5,10,7,8,9,8,3,5,1,2,9,8,10,5,1,3,3,2,3,2,7,3,6,7,8,5,10,6,4,8,1,4,8,8,7,10,1,5,6,10,2,7,2,5,5,9,7,1,4,6,6,6,8,7,9,7,3,1,5,7,7,5,9,7,2,3,5,5,1,2,2,2,7,2,9,10,10,3,5,5,2,3,1,2,1,10,5,4,10,7,6,7,8,10,5,1,4,9,4,7,6,7,10,5,7,6,9,5,2,10,1,9,6,6,4,10,4,8,10,6,5,6,8,10,8,4,2,8,9,6,8,8,10,4,5,3,8,1,4,3,9,2,9,2,9,9,5,2,6,10,1,4,10,6,9,10,5,10,5,8,9,10,1,7,7,8,8,1,6,1,8,4,4,2,1,1,6,5,9,3,3,8,5,1,4,3,8,9,3,10,4,6,7,6,3,2,5,3,7,6,8,2,6,10,9,9,5,3,1,4,7,7,9,8,10,7,5,7,4,1,8,7,7,6,7,7,8,5,4,2,4,3,2,6,3,6,6,1,4,6,8,7,9,6,2,1,7,9,5,1,3,5,3,8,9,2,6,5,8,1,10,4,10,3,2,4,9,8,7,1,2,6,10,1,3,3,7,9,8,2,5,1,7,1,1,6,5,9,3,5,1,6,9,8,6,10,1,2,4,10,4,3,6,9,6,4,5,8,10,7,4,3,3,7,2,1,4,2,5,6,6,9,1,2,10,9,6,5,10,4,4,9,1,9,3,2,3,6,6,4,2,7,7,4,8,7,3,2,2,7,2,2,8,10,10,8,5,8,6,7,3,8,4,1,4,8,5,5,2,4,3,3,5,7,2,3,5,9,8,2,7,1,2,7,7,6,2,6,1,5,7,2,8,6,7,4,9,9,2,6,3,8,8,1,5,4,8,2,5,10,7,3,9,5,8,10,3,10,5,6,10,9,4,1,8,7,3,8,6,8,9,8,8,6,9,8,2,10,1,6,2,1,2,6,5,10,9,2,5,5,10,10,10,7,10,5,1,1,6,10,7,7,7,4,8,6,5,10,9,8,10,9,5,8,5,5,2,6,7,1,8,8,7,5,10,9,3,8,5,6,7,7,4,10,7,7,4,10,2,6,6,2,5,7,2,4,2,6,10,4,2,2,3,2,2,2,8,8,3,1,7,6,3,6,6,3,1,10,1,8,2,9,2,7,10,5,4,10,6,10,2,2,3,6,5,3,10,8,9,6,7,3,7,1,10,5,1,4,5,5,1,4,4,3,6,10,10,10,10,4,3,9,2,9,1,8,9,4,4,1,8,5,4,2,6,7,2,8,10,10,6,7,7,9,3,4,10,1,2,1,8,9,1,1,3,5,10,8,2,9,2,6,7,4,5,3,6,9,3,9,5,1,9,9,2,7,4,2,6,5,5,3,6,4,3,5,5,8,9,6,9,10,6,4,8,6,6,1,10,9,4,7,5,8,4,1,7,10,10,1,2,9,9,2,7,9,1,1,3,3,1,1,9,9,10,5,1,7,1,6,2,9,10,1,6,6,9,7,10,7,3,8,4,4,4,7,7,2,9,7,1,4,6,5,3,6,1,7,10,6,8,9,3,9,5,2,6,6,6,10,5,9,5,7,2,1,10,6,8,7,1,2,9,2,6,2,6,8,8,2,9,4,8,3,8,7,3,6,1,1,9,2,1,4,8,9,4,7,3,8,5,8,3,10,9,1,4,10,2,3,9,8,10,10,4,10,4,2,3,1,2,4,2,9,5,5,8,6,10,8,5,2,6,2,5,7,7,4,1,4,2,7,10,8,3,1,7,9,6,6,2,5,8,9,10,3,4,2,8,4,8,3,1,6,6,5,10,5,5,2,9,1,2,6,4,9,2,10,8,5,9,5,6,2,5,3,2,6,3,6,2,8,3,6,5,7,9,1,10,3,7,1,1,10,7,4,8,1,6,8,7,5,6,3,5,1,1,1,6,2,7,5,8,2,2,9,8,10,10,6,7,1,1,4,8,5,5,10,6,6,8,5,8,3,2,10,7,10,3,5,2,5,7,10,9,6,9,6,9,10,5,1,9,5,1,6,8,9,7,10,8,10,4,10,9,4,2,9,3,3,10,7,3,3,3,8,6,10,3,8,2,1,9,2,7,2,7,4,5,1,2,8,6,3,1,8,7,5,2,10,6,7,10,8,6,6,9,7,1,2,9,2,8,6,5,2,6,10,7,3,10,8,7,8,5,8,1,5,9,8,7,10,2,8,6,10,4,2,2,7,8,7,1,3,9,10,4,6,10,9,7,5,10,10,1,4,10,1,6,3,8,6,1,6,9,9,9,6,9,3,10,7,1,4,8,4,9,3,1,4,6,10,10,7,1,3,5,6,7,1,5,3,8,6,1,1,6,2,1,5,1,7,6,10,5,5,6,10,6,6,9,8,8,1,4,5,6,3,4,7,8,6,8,1,9,4,5,5,3,3,5,3,1,2,10,6,7,2,9,8,8,6,9,7,8,2,2,3,5,4,9,9,8,10,8,4,5,7,2,5,4,1,9,7,2,2,9,4,3,3,3,8,5,1,8,7,1,8,5,7,7,4,5,6,5,9,5,5,4,8,8,1,10,2,4,4,2,10,7,1,8,4,10,7,4,2,3,4,10,9,3,1,9,3,1,2,7,9,3,4,2,3,1,2,8,2,6,5,4,10,7,3,2,10,8,6,2,2,3,6,5,3,1,4,7,4,8,3,1,9,2,6,2,5,8,3,4,5,8,1,4,6,6,5,9,3,1,6,1,10,9,9,2,10,6,10,6,1,6,2,4,6,6,4,6,3,5,10,2,9,6,5,8,7,9,5,8,9,3,4,2,2,5,2,4,1,10,10,2,4,2,1,10,6,7,7,3,10,10,2,5,1,6,8,6,10,9,4,7,5,4,4,10,8,6,5,3,6,3,5,7,8,2,10,3,1,1,2,10,6,4,4,8,6,6,2,8,2,5,4,5,3,8,3,4,6,8,7,5,7,5,5,4,8,1,7,2,7,3,2,1,10,2,10,9,10,10,10,8,5,10,3,10,8,7,4,1,5,6,9,7,5,6,3,6,3,5,2,10,4,1,2,7,9,4,10,4,7,8,1,2,6,7,10,10,8,5,8,4,1,4,8,6,6,2,5,9,8,1,6,3,5,6,6,9,9,2,2,10,1,10,9,4,8,9,3,6,1,1,10,2,4,7,5,6,3,7,6,6,9,8,3,5,1,6,9,5,3,1,10,5,10,8,3,2,7,1,4,4,1,9,4,7,9,4,2,5,10,5,8,10,6,9,1,3,10,3,8,3,1,7,9,5,7,2,1,5,4,6,7,7,4,4,3,1,9,6,6,1,9,6,3,5,2,4,4,5,3,8,9,2,2,2,3,7,8,1,8,1,10,8,6,10,9,2,10,2,9,2,5,5,6,9,4,7,8,5,10,7,3,7,7,6,1,1,6,3,1,7,10,5,4,2,9,7,9,10,2,4,10,7,5,8,7,7,3,3,1,3,8,10,9,1,8,4,7,4,6,9,1,9,5,2,10,10,3,8,4,8,4,9,6,4,3,10,7,8,10,2,8,1,1,7,9,5,8,3,5,10,8,1,4,1,8,6,6,5,4,3,2,8,5,10,5,8,3,3,9,7,2,5,5,3,7,6,1,1,10,9,3,7,10,3,5,8,1,9,1,1,3,1,9,6,8,6,2,10,6,8,7,10,8,8,3,7,2,1,7,3,5,3,10,10,10,1,2,2,9,2,8,7,7,1,5,2,1,5,6,5,7,6,10,1,4,9,6,8,8,6,2,7,5,1,6,9,6,8,9,8,2,4,10,8,5,3,1,8,1,9,10,8,4,5,1,2,2,9,1,7,2,6,10,1,6,2,2,9,2,2,2,3,4,7,6,7,7,7]
sol = Solution()
sol.wiggleSort(nums)
print(nums)

for i, num_temp in enumerate(nums[:-1]):
    if i%2 == 0 and nums[i] >= nums[i+1]:
        print("less",i,nums[i], nums[i+1])
    elif i%2 == 1 and nums[i] <= nums[i+1]:
        print("more",i,nums[i], nums[i+1])
