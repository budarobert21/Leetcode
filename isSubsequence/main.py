class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #

        # Approach 1
        length = len(t)
        last_length = len(t)
        index=[]
        for i in s:
            if i in t:
                print(length, t.index(i), last_length)

                index.append(length+t.index(i)- last_length)

                t = t[t.index(i)+1:]
                last_length = len(t)

            else:
                return False
        for i in range(len(index)-1):
            if index[i]>index[i+1]:
                return False
        return True


        # for i in s:
        #     if i in t:
        #         t = t[t.index(i)+1:]
        #     else:
        #         return False
        # return True

        #Copilot Method
        # i = 0
        # for c in t:
        #     if i < len(s) and s[i] == c:
        #         i += 1
        # return i == len(s)


if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    print(Solution().isSubsequence(s, t))

    s="aaaaaa"
    t="bbaaaa"
    print(Solution().isSubsequence(s, t))

    s="twn"
    t ="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxtxxxxxxxxxxxxxxxxxxxxwxxxxxxxxxxxxxxxxxxxxxxxxxn"
    print(Solution().isSubsequence(s, t))