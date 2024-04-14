class Solution(object):
    def isValid(self, nums):
        nums = [i for i in nums if i != '.']
        return len(set(nums)) == len(nums)
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # check rows
        for row in board:
            if not self.isValid(row):
                return False

        # check columns
        for col in zip(*board):
            if not self.isValid(col):
                return False

        # check sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.isValid(sub_box):
                    return False

        return True


if __name__ == '__main__':
   #  board = [[1, 2, 3],
   #           [4, 5, 6],
   #           [7, 8, 9]]
   # # print(Solution().isValidSudoku(board))
   #  print(board)
   #  print(*board)


    board = [["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]]
    print(Solution().isValidSudoku(board))