from typing import List
import time
class Solution:
    def help(self, ind , strs):
        if ind >= len(self.unique_letters) or len(strs) < 2:
            if strs != []:
                self.res.append(strs)
            return

        curr_letter = self.unique_letters[ind]
        letter_ct = {} 
        for word in strs:
            ct = word.count(curr_letter)
            if ct in letter_ct:
                letter_ct[ct].append(word)
            else:
                letter_ct[ct] = [word]

        for ct in letter_ct:
            self.help(ind + 1, letter_ct[ct])

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        self.unique_letters = []
        for word in strs:
            for char in [char for char in set(word) if char not in self.unique_letters]:
                self.unique_letters.append(char)

        self.res = []
        self.help(0 , strs)

        return self.res




sol = Solution()
print(sol.groupAnagrams(strs = ["lbj","tom","mci","vat","hep","eon","sal","doe","lot","ham","mop","bin","elf","sis","mob","maw","elk","hub","die","ran","tut","moe","bat","feb","bic","jim","hie","pat","pyx","fad","beg","non","meg","vat","irk","zap","tub","gal","ban","wan","shy","chi","ali"]))
