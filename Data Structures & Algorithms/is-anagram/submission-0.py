class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s)!=len(t)):
            return False

        hash_map_s = {}
        hash_map_t = {}      

        for char in s:
            if char not in hash_map_s:
                hash_map_s[char] = 1
            hash_map_s[char] += 1
            
        for char in t:
            if char not in hash_map_t:
                hash_map_t[char] = 1
            hash_map_t[char] += 1

        return hash_map_s==hash_map_t