class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixp = [1] * n
        suffixp = [1] * n

        prod = 1
        for i in range(n):
            prefixp[i] = prod
            prod *= nums[i]
        
        prod = 1
        for i in range(n):
            suffixp[n - 1 - i] = prod
            prod *= nums[n - 1 - i]
        
        ans = []

        for i in range(n):
            ans.append(prefixp[i] * suffixp[i])
        
        return ans