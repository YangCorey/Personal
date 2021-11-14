
from typing import List
class Solution:
    #25
    #20
    #8
    #1
    def coin(self, amount): #11, 2, 0

        if amount == 0:
            return 0
        elif amount < 0:
            return -1
        if amount in self.hist:
            return self.hist[amount]
        
        min_tot = float("inf")
        for coin in self.coins:
            #print(amount,ind, self.hist, "call", amount - (mul*self.coins[ind]), ind)
            res = self.coin(amount - coin)
            if res != -1 and (res + 1) < min_tot:
                min_tot = res + 1 

        min_tot = min_tot if min_tot != float("inf") else -1
        self.hist[amount] = min_tot

        return min_tot
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        #16
        #[2,3,8]
        self.hist = {0:0}
        self.tot_amount = amount
        for coin in coins:
            self.hist[coin] = 1
        coins.sort()
        self.coins = coins
        return self.coin(amount)

