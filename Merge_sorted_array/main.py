class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if (m == 0):
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
            print(nums1)
        elif (n != 0):
            for l in range(n):
                nums1[m + l] = nums2[l]
            print(nums1)

            ok = 1
            while ok == 1:
                ok = 0
                for i in range(len(nums1) - 1):
                    if nums1[i] > nums1[i + 1]:
                        nums1[i], nums1[i + 1] = nums1[i + 1], nums1[i]
                        ok = 1

        print(nums1)

#LEETCODE SOLUTION
    # for j in range(n):
    #     nums1[m + j] = nums2[j]
    # nums1.sort()

# si asta e faina
# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
#         while n >0:
#             if  m>0 and nums1[m-1]>=nums2[n-1]:
#                 nums1[n+m-1]=nums1[m-1]
#                 m-=1
#             else:
#                 nums1[n+m-1]=nums2[n-1]
#                 n-=1
#         return nums1


if __name__ == '__main__':
    print(Solution().merge([0], 0, [1], 1))
