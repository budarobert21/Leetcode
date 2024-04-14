class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[right]<target:
            return right
        else:
            return 0

        # if target in nums:
        #     return nums.index(target)
        # else:
        #     nums.append(target)
        #     nums.sort()
        #     return nums.index(target)
