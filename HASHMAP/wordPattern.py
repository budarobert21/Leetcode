class Solution(object):
    def wordPattern(self, pattern, s):
        # dictionary approach
        # Time complexity: O(n)
        # Space complexity: O(n)

        words = s.split(" ")
        if not len(words) == len(pattern):
            return False

        mapping = dict()  # key is the pattern, value is the word

        for i in range(len(words)):
            if pattern[i] not in mapping:
                # values() is a set - fast membership testing - O(1) amortised search
                if words[i] not in mapping.values():
                    mapping[pattern[i]] = words[i]
                else:
                    return False
            else:
                if not mapping[pattern[i]] == words[i]:
                    return False
        return True


# class Solution(object):
#     def wordPattern(self, pattern, s):
#         """
#         :type pattern: str
#         :type s: str
#         :rtype: bool
#         """
#
#         l = []
#         w = s.split()
#         for i in range(0, len(pattern)):
#             l.append(pattern[i])
#         if len(l) != len(w):
#             return False
#         else:
#             thing = set(zip(w, l))
#             return len(thing) == len(set(w)) == len(set(l))

if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
    print(Solution().wordPattern(pattern, s))

        #CoPilot
        # s_list = s.split()
        # pattern_list = list(pattern)
        # group = list(zip(pattern_list, s_list))
        # if len(s_list) != len(pattern_list):
        #     return False
        # for i in range(len(group)):
        #     if group[i][0] in pattern_list:
        #         pattern_list.remove(group[i][0])
        #     else:
        #         return False
        # return True