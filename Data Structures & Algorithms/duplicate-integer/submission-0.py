class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        appearance = set()

        for num in nums:
            if num in appearance:
                return True
            appearance.add(num)
        
        return False