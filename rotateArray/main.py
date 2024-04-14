class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
        # nums2 = nums[:]
        # n = len(nums)
        # for num in range(len(nums)):
        #     nums[(num+k)%n] = nums2[num]

        print(nums[n-k:],nums[:n-k])
        return nums



if __name__ == '__main__':
    s = Solution()
    print(s.rotate([1,2,3,4,5,6,7],3))
