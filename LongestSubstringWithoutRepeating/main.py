class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<1:
            return 0
        start = 0
        end = 1
        max_len = 1
        while end < len(s):
            #print(s[end], s[start:end ])
            if s[end] in s[start:end ]:
                if len(s[start:end]) > max_len:
                    max_len = len(s[start:end])
                start +=1
                end -=1


            end += 1

        if s[end-1] in s[start:end]:
            if len(s[start:end]) > max_len:
                max_len = len(s[start:end])


        return max_len





        # while end<len(s):
        #     if s[end] in s[start:end]:
        #         start+=1
        #     else:
        #         end+=1
        #         max_len=max(max_len,end-start)

        # CoPilot
        # if not s:
        #     return 0
        # start = 0
        # max_len = 0
        # used_char = {}
        # for i, c in enumerate(s):
        #     if c in used_char and start <= used_char[c]:
        #         start = used_char[c] + 1
        #     else:
        #         max_len = max(max_len, i - start + 1)
        #     used_char[c] = i
        # return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring("au"))
    print(s.lengthOfLongestSubstring("dvdf"))
