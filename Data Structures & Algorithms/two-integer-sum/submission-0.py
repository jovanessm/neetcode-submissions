class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetSum_index = {}
        for i in range(len(nums)):
            if nums[i] not in targetSum_index.keys():
                targetSum_index[target-nums[i]] = i
            else :
                return [targetSum_index[nums[i]],i]
