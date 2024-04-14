class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """


        dict={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        number=0
        for x in range(s.__len__()):
            if x<len(s)-1 and dict[s[x+1]]>dict[s[x]]:
                number-= dict[s[x]]
            else:
                number+=dict[s[x]]


        return number


if __name__ == '__main__':
    s = "IV"
    print(Solution().romanToInt(s))

    s = "IX"
    print(Solution().romanToInt(s))

    s = "LVIII"
    print(Solution().romanToInt(s))

    s = "MCMXCIV"
    print(Solution().romanToInt(s))

