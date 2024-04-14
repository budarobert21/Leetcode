class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_list = list(ransomNote)
        magazine_list = list(magazine)
        group= list(zip(magazine_list, ransom_list))
        if len(ransom_list) > len(magazine_list):
            return False
        for i in range(len(group)):
            if group[i][1] in magazine_list:
                magazine_list.remove(group[i][1])
            else:
                return False
        return True





        #Copilot
        # hash = {}
        #
        # for c in magazine:
        #     if c in hash:
        #         hash[c] += 1
        #     else:
        #         hash[c] = 1
        #
        # for c in ransomNote:
        #     if c not in hash or hash[c] == 0:
        #         return False
        #     hash[c] -= 1
        #
        # return True

if __name__ == '__main__':
    ransomNote = "aa"
    magazine = "aab"
    print(Solution().canConstruct(ransomNote, magazine))