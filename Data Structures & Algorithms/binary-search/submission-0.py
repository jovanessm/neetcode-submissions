class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        midIndex = int(len(nums) / 2)
        if nums[midIndex] == target:
            return midIndex
        if nums[midIndex] < target:
            return self.search(nums[0:midIndex], target)
        return self.search(nums[midIndex + 1:len(nums)], target)
        