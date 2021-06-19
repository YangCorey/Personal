class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        #3 [()()(),(()()), ((())),  (())(),()(())] 5
        #2 [()(), (())] 2 
        #1 [()] 1 
        res = set(["()"]) #()() (())
        ind = 1
        
        while ind < n: #n = 3
            #ind = 3
            temp_res = set(["()"*(ind+1)])
            #O()
            for poss in res:#(())
                #O(2n)
                open_ct = 0
                for char_ind, char in enumerate(poss):
                    if char == "(":
                        open_ct += 1
                        temp_res.add(poss[:char_ind+1] + "()" + poss[char_ind+1:]) 
                        if open_ct >= ind:
                            continue
            res = temp_res
            ind += 1
        return list(res)
