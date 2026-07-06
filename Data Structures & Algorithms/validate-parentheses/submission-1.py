class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {'}':'{', ']':'[', ')':'('}
        stack = []
        for p in range(len(s)):
            if s[p] in closeToOpen:
                if stack and stack[-1] == closeToOpen[s[p]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[p])
        # return True if stack is empty (enclosed), else false
        return True if not stack else False
