class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        n = len(citations)
        for i in range(n):
            if citations[i] >= n - i:
                return n - i


if __name__ == '__main__':
