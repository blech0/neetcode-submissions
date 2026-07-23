class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            product = 1
            for j in range(len(nums)):
                if j != i:
                    product *= nums[j]
            res.append(product)
        
        return res
