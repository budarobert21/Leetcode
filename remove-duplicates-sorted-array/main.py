class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 0):
            return 0
        index = 0
        for j in range(0,len(nums)):
            if (nums[j] != nums[index]):
                index += 1
                nums[index] = nums[j]

        return index + 1


# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         j = 1  # curr index where unique elemenet should be placed
#         for i in range(1, len(nums)):  # for each num
#             if nums[i] != nums[i - 1]:  # if not duplicate
#                 nums[j] = nums[i]  # add to unique array
#                 j += 1  # increment counter of unique elements
#         return j  # return count


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    s = Solution()
    print(s.removeDuplicates(nums))
