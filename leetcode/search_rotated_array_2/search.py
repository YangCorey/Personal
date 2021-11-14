class Solution:
    def search(self, nums, target: int) -> bool:
        #[3,3,5,5,6,7,8,2,2,3,4]
        #[2,2,2]
        #Conduct binary search on pivot by seraching for element that is less than or equal to the last element
        #and less than the element before it
        
        def pivot(start, end):
            if start == end:
                return [start, nums[start]]
            mid = (start+end)//2
            if nums[mid] < nums[end]:
                if mid == 0 or nums[mid-1] > nums[mid]:
                    return [mid, nums[mid]]
                else:
                    return pivot(start,mid-1)
            elif nums[mid] > nums[end]:
                return pivot(mid+1,end)
            else:
                return pivot(start,end-1)
        start_ind, val = pivot(0,len(nums)-1)
        nums = nums[start_ind:] + nums[:start_ind]
        print(nums)
        return 
sol = Solution()
sol.search(nums = [1,1,1,1,2,1], target = 0)
