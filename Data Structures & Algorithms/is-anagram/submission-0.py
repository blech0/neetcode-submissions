class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table1 = {}
        hash_table2 = {}
        for char in s:
            if char not in hash_table1:
                hash_table1[char] = 1
            else:
                hash_table1[char] += 1
        for char in t:
            if char not in hash_table2:
                hash_table2[char] = 1
            else:
                hash_table2[char] += 1

        if hash_table2 == hash_table1:
            return True

        return False