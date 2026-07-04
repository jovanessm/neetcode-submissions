class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # character counter
        s_dict = {}
        t_dict = {}

        for char_s in s:
            s_dict[char_s] = s_dict.get(char_s, 0) + 1
        
        for char_t in t:
            t_dict[char_t] = t_dict.get(char_t, 0) + 1

        return s_dict == t_dict