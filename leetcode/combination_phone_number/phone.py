from typing import List
class Solution:
    def help(self, ind):
        if ind >= len(self.digits) - 1:
            return self.num_map[self.digits[ind]]
        next_digit = self.help(ind+1)
        res = set()
        for char in self.num_map[self.digits[ind]]:
            for word in next_digit:
                res.add(char+word)
        return res

    def letterCombinations(self, digits: str) -> List[str]:
        self.digits = digits
        self.num_map = {}
        self.num_map["2"] = set(["a","b","c"])
        self.num_map["3"] = set(["d","e","f"])
        self.num_map["4"] = set(["g","h","i"])
        self.num_map["5"] = set(["j","k","l"])
        self.num_map["6"] = set(["m","n","o"])
        self.num_map["7"] = set(["p","q","r","s"])
        self.num_map["8"] = set(["t","u","v"])
        self.num_map["9"] = set(["w","x","y","z"])

        return list(self.help(ind = 0)) if len(digits) > 0 else []
        
        #Create an initial set with first digit
        #Create temp_set that will store the combinations
        #Iterate through the digits 1 - n then iterater through their characters
        #Iterate through each element in res set and append the digit character to current res
        #replace res with temp_set

sol = Solution()
print(sol.letterCombinations(digits = "23"))
