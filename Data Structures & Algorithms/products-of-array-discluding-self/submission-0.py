class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numOfZero = 0
        productOfAll = 1
        result = []

        # multiply everything
        for num in nums:
            if num == 0:
                numOfZero = numOfZero + 1
            else:
                productOfAll = productOfAll * num
    
        for num in nums:
            if numOfZero > 1:
                result.append(0)
            elif numOfZero == 1:
                result.append(productOfAll if num == 0 else 0)
            else:
                result.append(int(productOfAll/num))
        return result


