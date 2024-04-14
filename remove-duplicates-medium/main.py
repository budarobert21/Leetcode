class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)


        slow = 2
        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1


        return slow

# class Solution:
#     def removeDuplicates(self, nums):
#         j = 1
#         for i in range(1, len(nums)):
#             if j == 1 or nums[i] != nums[j - 2]:
#                 nums[j] = nums[i]
#                 j += 1
#         return j


if __name__ == '__main__':
    nums4 = [1, 2, 3, 4, 5]
    solution = Solution()
    solution.removeDuplicates(nums4)
    # print(nums4[:solution.removeDuplicates(nums4)])

    nums = [0, 0, 0, 0, 0]
    solution = Solution()
    solution.removeDuplicates(nums)
    # print(nums[:solution.removeDuplicates(nums)])

    nums1 = [1, 1, 1, 2, 2, 3]
    solution = Solution()
    solution.removeDuplicates(nums1)
    # print(nums1[:solution.removeDuplicates(nums1)])

    nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    solution = Solution()
    solution.removeDuplicates(nums2)
    # print(nums2[:solution.removeDuplicates(nums2)])

    nums3 = [1, 1]
    solution = Solution()
    solution.removeDuplicates(nums3)
# print(nums3[:solution.removeDuplicates(nums3)])
