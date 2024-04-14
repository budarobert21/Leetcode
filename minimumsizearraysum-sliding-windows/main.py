# class Solution(object): nu stiu de ce nu merge
#     def minSubArrayLen(self, target, nums):
#         """
#         :type target: int
#         :type nums: List[int]
#         :rtype: int
#         """
#         # Facuta de mine dar da time limit exceeded
#
#
#         left = 0
#         right = len(nums) - 1
#         sum = 0
#         lmin = len(nums)
#
#
#         for num in nums:
#             sum += num
#
#         if sum < target:
#             return 0
#         while left <= right and sum >= target:
#             if sum - nums[left] < sum - nums[right]:
#                 sum -= nums[right]
#                 right -= 1
#             else:
#                 sum -= nums[left]
#                 left += 1
#             lmin -= 1
#
#         return lmin + 1


# class Solution(object): #ce simpla e metoda asta
#         def minSubArrayLen(self, target, nums):
#             """
#             :type target: int
#             :type nums: List[int]
#             :rtype: int
#             """
#             l = 0
#             ret = float('inf')
#             tot = 0
#             for r in range(len(nums)):
#                 tot += nums[r]
#
#                 while tot >= target and l <= r:
#                     tot -= nums[l]
#                     ret = min(ret, r - l + 1)
#                     l += 1
#
#             return ret if ret != float('inf') else 0
if __name__ == '__main__':
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    s = Solution()
    print(s.minSubArrayLen(target, nums))
    nums = [1, 2, 3, 4, 5]
    target = 11
    s = Solution()
    print(s.minSubArrayLen(target, nums))

    nums = [2, 3, 4, 5, 1]
    target = 12
    s = Solution()
    print(s.minSubArrayLen(target, nums))

    # Copilot 2
    # n=len(nums)
    #
    # left=0
    # right=0
    # while right<n:
    #     if sum(nums[left:right+1])<target:
    #         right+=1
    #     else:
    #         break
    # if right==n:
    #     return 0
    # ans=right-left+1
    # while right<n:
    #     while sum(nums[left:right+1])>=target:
    #         left+=1
    #         ans=min(ans,right-left+1)
    #     right+=1
    # return ans
    #

    # copilot answer
    # n = len(nums)
    # ans = n + 1
    # left = 0
    # sum = 0
    # for right in range(n):
    #     sum += nums[right]
    #     while sum >= target:
    #         ans = min(ans, right - left + 1)
    #         sum -= nums[left]
    #         left += 1
    # return 0 if ans == n + 1 else ans

    # class Solution(object): ce simpla e metoda asta
    #     def minSubArrayLen(self, target, nums):
    #         """
    #         :type target: int
    #         :type nums: List[int]
    #         :rtype: int
    #         """
    #         l = 0
    #         ret = float('inf')
    #         tot = 0
    #         for r in range(len(nums)):
    #             tot += nums[r]
    #
    #             while tot >= target and l <= r:
    #                 tot -= nums[l]
    #                 ret = min(ret, r - l + 1)
    #                 l += 1
    #
    #         return ret if ret != float('inf') else 0

    # class Solution(object):
    #     def minSubArrayLen(self, target, nums):
    #         """
    #         :type target: int
    #         :type nums: List[int]
    #         :rtype: int
    #         """
    #         # Facuta de mine dar da time limit exceeded
    #         n = len(nums)
    #
    #         left = 0
    #         right = 0
    #         sum = 0
    #         lmin = n
    #         ok = 1
    #
    #         while right < n:
    #             sum += nums[right]
    #             # if sum>target:
    #             #     sum=0
    #             #     right=left
    #             #     left += 1
    #             if sum >= target:
    #                 ok = 0
    #                 if lmin > right - left + 1:
    #                     lmin = right - left + 1
    #                 sum = 0
    #                 right = left
    #                 left += 1
    #             right += 1
    #
    #         # if sum == target:
    #         #     if lmin > right - left + 1:
    #         #         lmin = right - left + 1
    #         #     sum = 0
    #         #     right = left
    #         #     left += 1
    #         if lmin == len(nums) and ok == 1:
    #             return 0
    #         return lmin
