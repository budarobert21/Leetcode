class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """




        #Metoda Simpla
        #return haystack.find(needle)
        #a doua netida sunoka
        # return haystack.index(needle) if needle in haystack else -1
        #a treia solutie
    #     #class Solution:
    # def strStr(self, haystack, needle):
    #     for i in range(len(haystack) - len(needle) + 1):
    #         if haystack[i:i+len(needle)] == needle:
    #             return i
    #     return -1