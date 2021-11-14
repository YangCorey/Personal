class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ind = 0 
        majority = None 
        tot = 0 
        #O(n)
        while ind + 1 < len(nums):
            if nums[ind] == nums[ind + 1]:
                if majority == nums[ind]:
                    tot += 1
                else:
                    if tot == 0:
                        majority = nums[ind]
                        tot += 1
                    else:
                        tot -= 1
            ind += 2
                        
        return majority if tot != 0 else nums[len(nums) - 1]
    
        #Solution:
        #Divide and conquer iteratively: If I know that n//2 + 1 elements will be the majority element
        #Then every non majority element will have a matching majority element
        #This will result in at least 1 extra majority element (if list is odd) or 2 (if list is even)
        #Then I can just check each pair of elements and see if majority or not and keep track

        #Facts:
        #List is n length
        #majority element (m) will appear n//2 + 1 times
        #If I take n//2 + 1 subsets of list, I will always have the majority in my subset
        #Medium will always equal majority
            #At most n//2 - 1 elements greater than or less than majoirty
        
        
        #Possigle solutions:

        
        
        
        #Order the list and count consecutive elements: O(nlog(n))
        
        #Create a hash: O(n) space: O(n)
        
        #divide and conquer - break elements into smaller groups and find majority of each group and build up
        #O(nlog(n))?
        #[1,1,1,1,2,2,2,2,2,2]
        #maj: 2 total: 1
        
        #[2,1,2,1,2,2,2,1,1]
        
        #Order half the elements and find medium? 
        
        #two pointer method? 
        
        #Taking the average? or Sum?
        
        #Apply a hash function to rearrange list?
        
        # 2/6 2/6 2/6
        # 1/6 1/6 1/6
        #n/3 []
        
