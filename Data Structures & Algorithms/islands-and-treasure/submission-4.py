class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols=len(grid),len(grid[0])
        q=deque()
        visit=set()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
                    visit.add((r,c))

        dist=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dist
                for x,y in directions:
                    nx,ny=r+x,c+y
                    if (nx<0 or nx==rows or ny<0 or ny==cols or (nx,ny) in visit or grid[nx][ny]==-1):
                        continue 
                    q.append((nx,ny))
                    visit.add((nx,ny))
            dist+=1

        
        