class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product=1
        zero_count=0
        for num in nums:
            if num!=0:
                product *= num
            else:
                zero_count+=1
        print(product)

        if zero_count<=1:
            for i in range(len(nums)):
                if nums[i]!=0 and zero_count==0 :
                    nums[i]=product//nums[i]
                else:
                    if nums[i]!=0:
                        nums[i]=0
                    else: nums[i]=product
        else:
            nums=[0]*len(nums)
        print(nums)
        return nums

    #mult mai bine creez o lista cu 0 rouri
    # n = len(nums)
    # ans = [0] * n
    # product = 1
    # zeros = 0
    #
    # for num in nums:
    #     if num == 0:
    #         zeros += 1
    #         continue
    #     product *= num
    #
    # if zeros == 1:
    #     for i in range(n):
    #         ans[i] = product if nums[i] == 0 else 0
    # elif zeros == 0:
    #     for i in range(n):
    #         ans[i] = product // nums[i]
    #
    # return ans
if __name__ == '__main__':
    nums=[1,2,3,4]
    Solution().productExceptSelf(nums)

    nums1 = [-1,1,0,-3,3]
    Solution().productExceptSelf(nums1)

    nums1 = [0,0]
    Solution().productExceptSelf(nums1)

    nums =[0, 4, 0]
    Solution().productExceptSelf(nums)