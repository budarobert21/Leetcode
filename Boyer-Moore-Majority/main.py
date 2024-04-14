class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return sorted(nums)[len(nums) / 2] # O(nlogn)
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1