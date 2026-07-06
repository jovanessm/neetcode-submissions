class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex = re.compile('[^a-zA-Z]')
        s = regex.sub('', s)
        s = s.lower()
        if len(s) == 0:
            return True
        leftIndex = 0
        rightIndex = len(s) - 1
        while(rightIndex > leftIndex):
            if s[leftIndex] != s[rightIndex]:
                return False
            leftIndex += 1
            rightIndex -= 1
        return True;


