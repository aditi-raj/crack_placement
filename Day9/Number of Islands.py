class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ans = 0
        n, m = len(grid), len(grid[0])

        def dfs(row, col):
            if grid[row][col] == '0':
                return 0
            else:
                grid[row][col] = '0'
                for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                    if 0 <= row+dy < n and 0 <= col+dx < m and grid[row+dy][col+dx] != '0':
                        dfs(row+dy, col+dx)
                return 1

        for row in range(n):
            for col in range(m):
                ans += dfs(row, col)

        return ans



        