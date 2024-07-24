class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m,n= len(image), len(image[0])
        initial=image[sr][sc]
        if initial==color:
            return image
        def dfs(sr,sc):
            image[sr][sc]=color
            for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                    if 0 <= sr+dy < m and 0 <= sc+dx < n and image[sr+dy][sc+dx] ==initial:
                        dfs(sr+dy,sc+dx)

        dfs(sr,sc)
        return image
        