class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left , right=0,len(numbers)-1
        while left<right:
            sum=numbers[left]+numbers[right]
            if(sum==target):
                return left+1,right+1
            elif sum<target:
                left+=1
            else:
                right-=1

        return []




if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum(numbers, target))

    numbers = [2, 3, 4]
    target = 6
    s = Solution()
    print(s.twoSum(numbers, target))


