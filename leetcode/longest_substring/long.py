class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        l = 0
        r = 0
        #O_space(n)
        char_index = {}
        #O(n)
        while r < len(s):#abca
            if s[r] in char_index:
                if char_index[s[r]] >= l:
                    l = char_index[s[r]] + 1
            char_index[s[r]] = r 
            r += 1
            if r - l > max_length:
                max_length = r-l
        return max_length
            
                
        
