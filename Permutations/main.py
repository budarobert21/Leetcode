class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtracking(index,path):
            if index==len(nums):
                permutations.append(path[:])
                return
            for i in range(len(path)+1):
                path.insert(i,nums[index])
                backtracking(index+1,path)
                path.pop(i)

        permutations=[]
        path=[]
        backtracking(0,path)
        return permutations