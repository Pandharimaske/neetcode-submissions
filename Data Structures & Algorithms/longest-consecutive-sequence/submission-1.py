class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums = list(set(nums))
        nums.sort()

        cnt = 1
        maxi = 1

        for i in range(1 , len(nums)):
            if nums[i] - nums[i - 1] == 1:
                cnt += 1
            else :
                cnt = 1
            
            maxi = max(maxi , cnt)
        
        return maxi