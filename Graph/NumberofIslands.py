class Solution(object):


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows=len(grid)
        columns=len(grid[0])
        def dfs( i, j):
            if i<0 or i>=rows or j<0 or j>=columns or grid[i][j]=="0" or grid[i][j]=="-1":
                return
            grid[i][j]="-1"
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i-1,j)

        count=0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]=="1":
                    dfs(i,j)
                    count+=1
        return count


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    s = Solution()
    print(s.numIslands(grid))

    grid = [ ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"]]
    print(s.numIslands(grid))
