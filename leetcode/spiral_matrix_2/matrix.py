def generateMatrix(n):
    res = []
    for _ in range(n):
        res.append([None]*n)
    
    x,y = 0,0
    dir =[
        [0,1],
        [1,0],
        [0,-1],
        [-1,0]
    ]
    val = 1
    ind = 0
    while  x >= 0 and x< n and y >= 0 and y < n and res[x][y] is None:
        res[x][y] = val
        val += 1
        if x+dir[ind][0] < 0 or x+dir[ind][0] >= n or y+dir[ind][1] < 0 or y+dir[ind][1] >= n or res[x+dir[ind][0]][y+dir[ind][1]] is not None:
            ind = (ind+1)%4
        x,y = x+dir[ind][0],y+dir[ind][1]
    return res

generateMatrix(3)
