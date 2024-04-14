class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(start, path):
            if len(path) == k:
                res.append(path)
                return
            for i in range(start, n+1):
                backtrack(i+1, path+[i])

        res = []
        backtrack(1, [])
        return res






        # def backtracking(index,path):
        #     if len(path)==k:
        #         combinations.append(path[:])
        #         return
        #     for i in range(index,n+1):
        #         path.append(i)
        #         backtracking(i+1,path)
        #         path.pop()
        #
        # combinations=[]
        # path=[]
        # backtracking(1,path)
        # return combinations
if __name__ == '__main__':
    n = 4
    k = 2
    s = Solution()
    print(s.combine(n,k))
