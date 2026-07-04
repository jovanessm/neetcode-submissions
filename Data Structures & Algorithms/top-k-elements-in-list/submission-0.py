class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(list)
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        items = list(dic.items())
        items.sort(key=lambda x:x[1], reverse=True)
        # return list of num from items[:k]
        # [expression for item in iterable]
        return [num for num, req in items[:k]]
