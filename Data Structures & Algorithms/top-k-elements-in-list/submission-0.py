class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        freq = [[val , key] for key , val in count.items()]
        freq.sort(reverse=True)
        ans = []
        for i in range(k):
            ans.append(freq[i][1])
        
        return ans