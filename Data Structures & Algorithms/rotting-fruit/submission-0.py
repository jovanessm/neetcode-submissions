class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # use BFS
        # iterate through the grid -> check for fresh and add rotten to queue
        # save the maxtime rotten in the queue to maintain the max
        # then starts to floodfill 

        row, col = len(grid), len(grid[0])
        max_time = 0
        queue_rotten = deque()
        freshCounter = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue_rotten.append((r,c, max_time))
                elif grid[r][c] == 1:
                    freshCounter += 1

        direction = [(0,1), (0,-1), (1,0), (-1,0)]

        while(queue_rotten):
            r, c, time = queue_rotten.popleft()
            max_time = max(time, max_time)

            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    freshCounter -= 1
                    grid[nr][nc] = 2
                    queue_rotten.append((nr, nc, time + 1))
        
        return max_time if freshCounter == 0 else -1
                




