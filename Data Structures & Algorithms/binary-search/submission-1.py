class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper (left, right):
            curIndex = int((left + right)/2)
            if left > right:
                return -1
            if nums[curIndex] == target:
                return curIndex
            if nums[curIndex] > target:
                return helper(left, curIndex - 1)
            return helper(curIndex + 1, right)
        return helper(0, len(nums)-1)
        