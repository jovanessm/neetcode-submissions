class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        # Edge Case if length of list is 0
        if len(strs) == 0:
            return result
        # Save the length of every string first
        for st in strs:
            result = result + str(len(st)) + ','
        # divider between length and real content
        result = result + '#'
        # Append the strings
        for st in strs:
            result = result + st
        return result

    def decode(self, s: str) -> List[str]:
        resList = []
        if s == "#":
            return ["#"]
        
        length, content = s.split('#')

        lengthList = length.split(',')[:-1]

        for leng in lengthList:
            resList.append(content[0:int(leng)])
            content = content[int(leng):]
        
        return resList

