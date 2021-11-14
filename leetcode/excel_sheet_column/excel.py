class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        #Create a hash with upper case letters as key and 1 - 26 value respectively
        #Iterate backwards through columnTitle starting from last letter and multiple the current letter value by
        #26^i where i = len(columnTitle) - curr_pos
        
        
        #O(1)
        #Space O(1)
        letter_val = {}
        for ind, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            letter_val[letter] = (ind + 1)
        
        ind = len(columnTitle)
        tot = 0
        multiplier = 1
        while ind > 0: 
            ind -= 1
            tot += letter_val[columnTitle[ind]] * multiplier 
            multiplier *= 26 
            
        return tot
            
