class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if not digits:
            return []
        if len(digits)==1:
            return list(phone[digits])

        def backtracking(index,path):
            if index==len(digits):
                combinations.append(''.join(path))
                return
            for i in phone[digits[index]]:
                path.append(i)
                backtracking(index+1,path)
                path.pop()


        combinations=[]
        path=[]
        backtracking(0,path)
        return combinations

if __name__ == '__main__':
    digits = "2"
    s = Solution()
    print(s.letterCombinations(digits))


        #CoPilot
        # if not digits:
        #     return []
        #
        # phone = {
        #     '2': 'abc',
        #     '3': 'def',
        #     '4': 'ghi',
        #     '5': 'jkl',
        #     '6': 'mno',
        #     '7': 'pqrs',
        #     '8': 'tuv',
        #     '9': 'wxyz'
        # }
        #
        # def backtrack(index, path):
        #     if index == len(digits):
        #         combinations.append(''.join(path))
        #         return
        #     for letter in phone[digits[index]]:
        #         path.append(letter)
        #         backtrack(index + 1, path)
        #         path.pop()
        #
        # combinations = []
        # backtrack(0, [])
        # return combinations