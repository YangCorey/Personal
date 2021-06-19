class Solution:
    def perm(self, val):

        print(val)
        tot = 1
        while val > 1:
            tot *= val
            val -= 1
        print(tot)
        return tot

    def uniquePaths(self, m: int, n: int) -> int:
        tot = m-1 + n-1
        return self.perm(tot) / (self.perm(m-1)* self.perm(tot-(m-1)))

 
