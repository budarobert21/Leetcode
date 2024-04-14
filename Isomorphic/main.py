# Given
# two
# strings
# s and t, determine if they
# are
# isomorphic.
#
# Two
# strings
# s and t
# are
# isomorphic if the
# characters in s
# can
# be
# replaced
# to
# get
# t.
#
# All
# occurrences
# of
# a
# character
# must
# be
# replaced
# with another character while preserving the order of characters.No two characters may map to the same character, but a character may map to itself.
#
# Example
# 1:
#
# Input: s = "egg", t = "add"
# Output: true
# Example
# 2:
#
# Input: s = "foo", t = "bar"
# Output: false
# Example
# 3:
#
# Input: s = "paper", t = "title"
# Output: true
#
# Constraints:
#
# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t
# consist
# of
# any
# valid
# ascii
# character.
class Solution(object):
    def occurence(self, s):
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]]+=1
        return d


    def list_converted(self, s,l):
        i = 0;
        d=self.occurence(s)
        l = [0] * len(s)
        for v in range(len(d)):
            i += 1
            for j in range(len(s)):
                if s[j] == list(d.keys())[i-1]:
                    l[j] = i
        return l



    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        d1 = self.list_converted(s, [])
        d2 = self.list_converted(t, [])
        if (len(s) != len(t) or d1!=d2):
            return False
        for i in range(len(s)):
            if s[i] in d1 and t[i] in d2:
                if d1[s[i]] != d2[t[i]]:
                    return False
        return True
    # def isIsomorphic(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: bool
    #     """
    #     return [s.find(i) for i in s] == [t.find(j) for j in t]


#LEETCODE SOLUTION
# class Solution(object):
#     def occurence(self, s):
#         d = {}
#         for i in range(len(s)):
#             if s[i] not in d:
#                 d[s[i]] = i
#         return d
#
#     def isIsomorphic(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         if len(s) != len(t):
#             return False
#
#         d1 = self.occurence(s)
#         d2 = self.occurence(t)
#
#         for i in range(len(s)):
#             if d1[s[i]] != d2[t[i]]:
#                 return False
#
#         return True

if __name__ == '__main__':
    # s = "egg"
    # t = "add"
    # print(Solution().occurence("egg"))
    # print(Solution().isIsomorphic2(s, t))
    #
    # s = "foo"
    # t = "bar"
    # print(Solution().isIsomorphic2(s, t))

    s = "paper"
    t = "title"
    print(Solution().occurence("paper"))
    print(Solution().occurence("title"))
    print(Solution().list_converted("paper", []))
    print(Solution().list_converted("title", []))
    print(Solution().isIsomorphic(s, t))

