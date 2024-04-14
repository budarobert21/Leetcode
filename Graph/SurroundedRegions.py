class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        #         Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
        #
        # A region is captured by flipping all 'O's into 'X's in that surrounded region.
        # eu puteam sa incep din exterior si sa gasesc toate regiunile care sunt inconjurate de X si sa le marchez cu -1



        #caut 0 urile din exterior si merg cu dfs astfel marchez toate 0 urile conectate care sunt inconjurate de X cu -1


        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=columns or board[i][j]=="X" or board[i][j]=="-1":
                return
            board[i][j]="-1"
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i-1,j)

        rows=len(board)
        columns=len(board[0])
        for i in range(rows):
            for j in range(columns):
                if i==0 or i==rows-1 or j==0 or j==columns-1:
                    dfs(i,j)
        for i in range(rows):
            for j in range(columns):
                if board[i][j]=="-1":
                    board[i][j]="O"
                else:
                    board[i][j]="X"
        return board


if __name__ == '__main__':
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    s = Solution()
    s.solve(board)
    print("=====================================")
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "X", "O", "X"]
    ]
    s.solve(board)
    print("=====================================")
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "X", "X", "O"]
    ]
    s.solve(board)
    print("=====================================")
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["O", "X", "X", "X"]
    ]
    s.solve(board)
    print("=====================================")
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["O", "O", "X", "X"]
    ]
    s.solve(board)
    print("=====================================")
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["O", "O", "X", "O"]
    ]
    s.solve(board)
    print("=====================================")
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["O", "O", "X", "O"]
    ]
    s.solve(board)
    print("=====================================")
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["O", "O", "X", "X"]]

    s.solve(board)
    print("=====================================")
