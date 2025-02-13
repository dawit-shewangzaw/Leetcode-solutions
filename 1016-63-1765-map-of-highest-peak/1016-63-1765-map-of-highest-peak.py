class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        d=((0,1),(1,0),(-1,0),(0,-1))
        m,n=len(isWater),len(isWater[0])
        q=deque()
        res=[[-1]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if(isWater[i][j]==1):
                    res[i][j]=0
                    q.append((i,j))
        t=1
        while(q):
            for _ in range(len(q)):
                r,c=q.popleft()
                for dx,dy in d:
                    nr,nc=r+dx,c+dy
                    if(0<=nr<m and 0<=nc<n and res[nr][nc]==-1):
                        q.append((nr,nc))
                        res[nr][nc]=t
            t+=1
            
        return res