class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_dict = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'}


        result = ''
        old_key=1000
        for  key in sorted(roman_dict.keys(),reverse=True):
            n=num
            count=1

            #i want the old key before this one



            if old_key>1:
                while n>10:
                    n//=10
                    count*=10
                if old_key-n*count==count:
                    result+=roman_dict[count]
                    result+=roman_dict[old_key]
                    num-=n*count

            while num >=key:
                result+=roman_dict[key]
                num-=key
            old_key=key




        return result




if __name__ == '__main__':
    num=1994
    print(Solution().intToRoman(num))











        # # 1. Initialize the dictionary
        # roman_dict = {
        #     1: 'I',
        #     4: 'IV',
        #     5: 'V',
        #     9: 'IX',
        #     10: 'X',
        #     40: 'XL',
        #     50: 'L',
        #     90: 'XC',
        #     100: 'C',
        #     400: 'CD',
        #     500: 'D',
        #     900: 'CM',
        #     1000: 'M'
        # }
        #
        # # 2. Initialize the result
        # result = ''
        #
        # # 3. Iterate the dictionary in reverse order
        # for key in sorted(roman_dict.keys(), reverse=True):
        #     while num >= key:
        #         result += roman_dict[key]
        #         num -= key
        #
        # return result