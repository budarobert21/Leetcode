class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i + 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results
    # Mai usoara cu set si nu ne mai stresam de duplicate
    # class Solution:
    #     def threeSum(self, nums: List[int]) -> List[List[int]]:
    #         target = 0
    #         nums.sort()
    #         s = set()
    #         output = []
    #         for i in range(len(nums)):
    #             j = i + 1
    #             k = len(nums) - 1
    #             while j < k:
    #                 sum = nums[i] + nums[j] + nums[k]
    #                 if sum == target:
    #                     s.add((nums[i], nums[j], nums[k]))
    #                     j += 1
    #                     k -= 1
    #                 elif sum < target:
    #                     j += 1
    #                 else:
    #                     k -= 1
    #         output = list(s)
    #         return output

    # def threeSum(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #
    #     results = []
    #     nums.sort()
    #     for i in range(len(nums) - 2):
    #         if i > 0 and nums[i] == nums[i - 1]:
    #             continue
    #         l, r = i + 1, len(nums) - 1
    #         while l < r:
    #             s = nums[i] + nums[l] + nums[r]
    #             if s < 0:
    #                 l += 1
    #             elif s > 0:
    #                 r -= 1
    #             else:
    #                 results.append((nums[i], nums[l], nums[r]))
    #                 while l < r and nums[l] == nums[l + 1]:
    #                     l += 1
    #                 while l < r and nums[r] == nums[r - 1]:
    #                     r -= 1
    #                 l += 1
    #                 r -= 1
    #     return results

























if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    print(solution.threeSum(nums))



