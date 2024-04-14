class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n=len(matrix)-1
        m=len(matrix[0])-1

        left=0
        right=m
        i=0
        while i<n+1 and left<=right:
            if matrix[i][m]<target:
                i+=1
                left=0
                right=m
                continue
            else:
                mid=(left+right)//2
                if matrix[i][mid]<target:
                    left=mid+1
                elif matrix[i][mid]>target:
                    right=mid-1
                else:
                    return True

        return False


# class Solution(object):
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         if len(matrix) == 0:
#             return False
#         rowSize = len(matrix)
#         colSize = len(matrix[0])
#         left = 0
#         right = rowSize * colSize - 1
#
#         while left <= right:
#             mid = (left + right) // 2
#             row = mid // colSize
#             col = mid % colSize
#
#             if (matrix[row][col] < target):
#                 left = mid + 1
#             elif (matrix[row][col] > target):
#                 right = mid - 1
#             else:
#                 return True
#         return False


if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    s = Solution()
    print(s.searchMatrix(matrix,target))