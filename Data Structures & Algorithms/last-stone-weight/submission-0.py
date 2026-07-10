import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-n for n in stones]
        heapq.heapify(stones)

        while len(stones) > 1 :
            largest1 = -heapq.heappop(stones)
            largest2 = -heapq.heappop(stones)
            largest1 -= largest2
            if largest1 > 0:
                heapq.heappush(stones, -largest1)
        
        return -stones[0] if len(stones) == 1 else 0