class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        for i in range(len(strs[0])):
            prefix = strs[0][:len(strs[0]) - i]
            if all(prefix in s[:len(prefix)] for s in strs[1:]):
                return prefix
        return ""


        #Metoda misto leetcode
        # class Solution(object):
        #     def longestCommonPrefix(self, strs):
        #
        #         """
        #         :type strs: Lis
        #         t[str]
        #         :rtype: str
        #         """
        #         l = list(zip(*strs))
        #         prefix = ""
        #         for i in l:
        #             if len(set(i)) == 1:
        #                 prefix += i[0]
        #             else:
        #                 break
        #         return prefix
        #Copilot
        # if not strs:
        #     return ""
        #
        # for i in range(len(strs[0])):
        #     for string in strs[1:]:
        #         if i >= len(string) or string[i] != strs[0][i]:
        #             return strs[0][:i]
        #
        # return strs[0]



if __name__ == '__main__':
    strs=["a","a","b"]
    print(Solution().longestCommonPrefix(strs))