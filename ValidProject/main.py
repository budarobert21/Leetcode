class Solution(object):
        def isPalindrome(self, s):
                """
                :type s: str
                :rtype: bool
                """

                s = "".join(filter(lambda x: x.isalnum(), s)).lower()
                if s == s[::-1]:
                        return True
                return  False





if __name__ == '__main__':
        s = "A man, a plan, a canal: Panama"
        print(Solution().isPalindrome(s))
