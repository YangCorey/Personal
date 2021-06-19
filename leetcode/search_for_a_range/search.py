class Solution:
          
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1,-1]
        if len(nums) == 0:
            return res

        left, right = 0, len(nums) - 1
        
        found = False
        while left <= right: 
            mid = (right+left)//2
            if nums[mid] == target:
                found = True
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if not found:
            return res
        
        left_r = left 
        right_r = right

 

        if mid == 0 or nums[mid - 1] != target:
            res[0] = mid
        else:
            while left <= right:
                mid = (right+left)//2
                if nums[mid] == target:
                    if mid-1 < 0 or nums[mid-1] != target:
                        res[0] = mid
                        break
                    else:
                        right = mid - 1
                else:
                    left = mid + 1
                    
        if res[0] == -1:
            res[0] = 0
                    

        left = left_r
        right = right_r
        mid = (left+right)//2
        if mid == len(nums) - 1 or nums[mid+1] != target:
            res[1] = mid
        else:
            while left <= right:
                mid = (right+left)//2
                if nums[mid] == target:
                    if mid+1 >= len(nums) or nums[mid+1] != target:
                        res[1] = mid
                        break
                    else:
                        left = mid + 1
                else:
                    right = mid - 1
        if res[1] == -1:
            res[1] = 0
            
        return res
