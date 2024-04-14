class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) <= 1:
            return True

        if nums[0] == 0:
            return False
        leap = 0
        count = 0
        for n in nums:
            if n > leap:
                leap = n
            elif n == 0 and leap < 1 and count != len(nums) - 1:
                return False
            leap -= 1
            count += 1

        return True

#Metoda super
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         goal = len(nums) - 1
#
#         for i in range(len(nums) - 2, -1, -1):
#             if i + nums[i] >= goal:
#                 goal = i
#
#         return True if goal == 0 else False

if __name__ == '__main__':
    nums = [2,3,1,1,4]
    print(Solution().canJump(nums))

    nums = [3,2,1,0,4]
    print(Solution().canJump(nums))

    nums = [2,0,0]
    print(Solution().canJump(nums))