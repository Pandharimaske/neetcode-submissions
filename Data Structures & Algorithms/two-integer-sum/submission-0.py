class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seenIdx = dict()

        for i , num in enumerate(nums):
            rem = target - num
            if rem in seenIdx:
                return [seenIdx[rem] , i]
            
            seenIdx[num] = i
        
        return [-1 , -1]
        