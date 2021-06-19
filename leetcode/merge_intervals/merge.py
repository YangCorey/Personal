from typing import List
class Solution:
    def merge_sort(self,intervals):
        if len(intervals) <= 1:
            return intervals
        left_res = self.merge_sort(intervals[:len(intervals)//2])
        right_res = self.merge_sort(intervals[len(intervals)//2:])
        
        left_ind = 0 # 0
        right_ind = 0# 1
        res = [] #[[0,4],[1,4]]
        while left_ind < len(left_res) or right_ind < len(right_res):
            left_val = left_res[left_ind][0] if left_ind < len(left_res) else right_res[right_ind][0] + 1
            right_val = right_res[right_ind][0] if right_ind < len(right_res) else left_res[left_ind][0] + 1
            
            if left_val < right_val:
                res.append(left_res[left_ind])
                left_ind += 1
            else:
                res.append(right_res[right_ind])
                right_ind += 1
                
        return res
                    
        
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = self.merge_sort(intervals = intervals)
        print(intervals)
        res = [intervals[0]] 
        for ind in range(1, len(intervals)):#1 2 3
            print(intervals[ind])
            if res[len(res)-1][1] >= intervals[ind][0]:
                res[len(res)-1][1] = max(intervals[ind][1],res[len(res)-1][1])
            else:
                res.append(intervals[ind])

        return res

        #Recursively split list until 1 element
        #compare the minimum of both list
            #If overlap, merge and add to res
            #otherwise find the min and add to res
            #repeat until both left and right are empty
            

sol = Solution()
print(sol.merge(intervals = [[1,4],[1,5]]))
