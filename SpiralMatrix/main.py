class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        #o sa folosim ok care schimba directia de la 0 pana la 3
        # 0 -> dreapta, 1 -> jos, 2 -> stanga, 3 -> sus

        # i si j sunt coordonatele

        # n si m sunt dimensiunile matricei
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []


        left=0
        top=0
        bottom = len(matrix)-1
        right = len(matrix[0])-1
        # rezultatul
        result = []
        # daca n sau m sunt 0, atunci returnam lista goala
        # if bottom == 0 and right == 0:
        #     return []

        while top <= bottom and left <= right:
            for j in range(left,right+1):
                result.append(matrix[top][j])
            for i in range(top+1,bottom+1):
                result.append(matrix[i][right])
            if top < bottom and left < right:
                for j in range(right-1,left,-1):
                    result.append(matrix[bottom][j])
                for i in range(bottom,top,-1):
                    result.append(matrix[i][left])
            top+=1
            bottom-=1
            left+=1
            right-=1
        return result


















if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,3,6,9,8,7,4,5]

    print(s.spiralOrder([[1]])) # [1,2,3,4,8,12,11,10,9,5,6,7]
        # Copilot
        # if not matrix:
        #     return []
        # m, n = len(matrix), len(matrix[0])
        # top, bottom, left, right = 0, m - 1, 0, n - 1
        # res = []
        # while top <= bottom and left <= right:
        #     for j in range(left, right + 1):
        #         res.append(matrix[top][j])
        #     for i in range(top + 1, bottom + 1):
        #         res.append(matrix[i][right])
        #     if top < bottom and left < right:
        #         for j in range(right - 1, left, -1):
        #             res.append(matrix[bottom][j])
        #         for i in range(bottom, top, -1):
        #             res.append(matrix[i][left])
        #     top += 1
        #     bottom -= 1
        #     left += 1
        #     right -= 1
        # return res