class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) > 0:
            i = 0
            j = len(nums) - 1

            while i <= j:
                if nums[i] == val:
                    nums[i], nums[j] = nums[j], nums[i]
                    j -= 1
                else:
                    i += 1

            while nums and nums[-1] == val:
                nums.pop()

        return len(nums)

if __name__ == '__main__':
    Solution().removeElement([4,5], 4)
    print(Solution().removeElement([3, 2, 2, 3], 3))




# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#         k = 0
#         for i in range(len(nums)):
#             if nums[i] == val:
#                 nums[i] = '_'
#             else:
#                 k += 1
#         nums.sort()
#         return k

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         index = 0
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[index] = nums[i]
#                 index += 1
#         return index






#chatgpt SOLUTION
# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#         if len(nums) == 0:
#             return 0
#
#         left = 0
#         right = len(nums) - 1
#
#         while left <= right:
#             if nums[left] == val:
#                 nums[left], nums[right] = nums[right], nums[left]
#                 right -= 1
#             else:
#                 left += 1
#
#         return left
#
#
# if __name__ == '__main__':
#     sol = Solution()
#     print(sol.removeElement([1], 1))  # Output: 0
#     print(sol.removeElement([3, 2, 2, 3], 3))  # Output: 2