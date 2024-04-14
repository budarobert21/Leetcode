# You are given an integer array prices where
# prices[i] is the price of a given stock on the ith day.
#
# On each day, you may decide to buy and/or sell the stock.
# You can only hold at most one share of the stock at any time. However,
# you can buy it then immediately sell it on the same day.
#
# Find and return the maximum profit you can achieve.



class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy=prices[0]
        ans=0
        for i in range(1,len(prices)):
            if(prices[i]<prices[i-1]): #Daca se gaseste o crestere
                ans+=prices[i-1]-buy
                buy=prices[i]



# leetcode solution much simpler
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         pro = 0
#         cur = prices[0]
#         for i in range(1, len(prices)):
#             if cur < prices[i]:
#                 pro += prices[i] - cur
#             cur = prices[i]
#         return pro


if __name__ == '__main__':
