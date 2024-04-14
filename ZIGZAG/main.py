class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        #Practic ce facem este sa facem 3 randuri si noi punem cate un element pe fiecare rand in coloana cand ajungem la final schimbam directia si tot asa
        rows = [""] * numRows


        index = 0
        change_direction = True
        for i in range(len(s)):
            rows[index] += s[i]

            if change_direction:
                index += 1
            else:
                index -= 1

            if (index == 0):
                change_direction = True
            elif index == numRows - 1:
                change_direction = False



        return ''.join(rows)


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    print(Solution().convert(s, numRows))

    # cOPILOT SOLUTION
    # if numRows == 1:
    #     return s
    # res = [''] * numRows
    # index = 0
    # step = 1
    # for c in s:
    #     res[index] += c
    #     if index == 0:
    #         step = 1
    #     elif index == numRows - 1:
    #         step = -1
    #     index += step
    # return ''.join(res)

if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    print(Solution().convert(s, numRows))
