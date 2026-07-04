class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make a dict with key = sorted, 
        # value is a list with unsorted strings, 
        # and return dict values
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        return list(groups.values())
