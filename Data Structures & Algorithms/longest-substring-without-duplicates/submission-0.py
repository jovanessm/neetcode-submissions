class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        length = 0
        back_index = 0
        last_seen = {}

        for front_index in range(len(s)):
            char = s[front_index]
            if char in last_seen and last_seen[char] >= back_index:
                back_index = last_seen[char] + 1
            last_seen[char] = front_index
            length = max(length, front_index - back_index + 1)

        return length