from collections import deque


class Solution(object):


    def snakesAndLadders(self, board):
        def coord(self, number, n):

            i = 0
            j = 0

            if number % n == 0:
                i = n - number // n
                if number // n % 2 == 0:
                    j = 0
                else:
                    j = n - 1

            else:
                i = n - number // n - 1
                j = number % n - 1 if i % 2 == 1 else n - number % n

            return [i, j]

        length=len(board)
        queue=deque()
        queue.append([1,0])
        visit=set()
        while queue:
            square,move=queue.popleft()
            for i in range(1,7):
                nextMove=square+i
                r,c =coord(self,nextMove,length)
                if board[r][c]!=-1:
                    nextMove=board[r][c]
                if nextMove==length*length:
                    return move+1
                if board[r][c] not in visit:
                    visit.add(nextMove)
                    queue.append([nextMove,move+1])
        return -1









    # Cu DFS
    # def snakesAndLadders(self, board):
    #     """
    #     :type board: List[List[int]]
    #     :rtype: int
    #     """
    #     rows = len(board)
    #     columns = len(board[0])
    #     def dfs(i, j):
    #         if i < 0 or i >= rows or j < 0 or j >= columns or board[i][j] == -1 or board[i][j] == -2:
    #             return
    #         board[i][j] = -2
    #         dfs(i, j + 1)
    #         dfs(i, j - 1)
    #         dfs(i + 1, j)
    #         dfs(i - 1, j)
    #     count = 0
    #     for i in range(rows):
    #         for j in range(columns):
    #             if board[i][j] != -1:
    #                 dfs(i, j)
    #                 count += 1
    #     return count


if __name__ == '__main__':
    board = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1]
    ]
    board_length=len(board)

    s = Solution()

    print(s.snakesAndLadders(board))

    board =[[-1, 7, -1], [-1, 6, 9], [-1, -1, 2]]
    print(s.snakesAndLadders(board))