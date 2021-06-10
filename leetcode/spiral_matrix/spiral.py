from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        step = [[0,1], [1,0], [0,-1], [-1,0]]
        res = []
        curr = [0,0]
        vlim = [0, len(matrix)]
        hlim = [0, len(matrix[0])]

        step_count = 0
        while vlim[0] < vlim[1] and hlim[0] < hlim[1]:
            while vlim[0] <= curr[0] and curr[0] < vlim[1] and hlim[0] <= curr[1] and curr[1] < hlim[1]:
                res.append(matrix[curr[0]][curr[1]])
                curr[0] += step[step_count][0]
                curr[1] += step[step_count][1]

            curr[0] -= step[step_count][0]
            curr[1] -= step[step_count][1]

            if step_count == 0:
                vlim[0] += 1
            elif step_count == 1:
                hlim[1] -= 1
            elif step_count == 2:
                vlim[1] -= 1
            else:
                hlim[0] += 1
            step_count = (step_count+1)%4
            curr[0] += step[step_count][0]
            curr[1] += step[step_count][1]


        return res



sol = Solution()
for x in range(5,1,-1):
    print(x)
print(sol.spiralOrder([[1,2,3,4],[1,2,3,4]]))
