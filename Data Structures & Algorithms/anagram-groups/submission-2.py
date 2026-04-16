class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = dict()
        for s in strs:
            hash_table = [0] * 26
            for char in s:
                hash_table[ord(char)-97] += 1
            hash_tuple = tuple(hash_table)
            if hash_tuple not in hash_map:
               (hash_map[hash_tuple]) = [s]
            else:
                hash_map[hash_tuple].append(s)
        result = list(hash_map.values())
        return result