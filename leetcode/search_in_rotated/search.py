class Solution:
    def search(self, nums: List[int], target: int) -> int:        
        left = 0
        right = len(nums) - 1
        mid = (len(nums) - 1) // 2
        if nums[len(nums) - 1] < nums[0]:
            while mid+1 < len(nums) and nums[mid+1] > nums[mid]:
                if nums[mid] < nums[len(nums) - 1]:
                    right = mid - 1
                else:
                    left = mid + 1
                mid = (right+left)//2

            #mid will equal max_index after loop
            if target >= nums[0]:
                left = 0
                right = mid 
            else:
                left = mid + 1 
                right = len(nums) - 1
            
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1#4
        return -1
                
                
