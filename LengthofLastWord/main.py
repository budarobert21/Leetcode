class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                length+=1
            elif length > 0 and s[i] == ' ':
                break

        return length


        #Copilot
        #return len(s.strip().split(' ')-1])



if __name__ == '__main__':
    s = "Hello World"
    print(Solution().lengthOfLastWord(s))
