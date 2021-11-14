class Solution:
    def isHappy(self, n: int) -> bool:
        hist = set()

        def square_sum(val):
            tot = 0
            while val > 0:
                tot += (val%10)**2
                val // 10
            return tot
        while n != 1:
            print(n)
            n = square_sum(n)
            if n in hist:
                return False
            hist.add(n)
        return True
            
sol = Solution()
sol.isHappy(19)
