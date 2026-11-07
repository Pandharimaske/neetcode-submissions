class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seenidx = {}
        l , r = 0 , 0
        maxi = 0

        while r < n:
            if s[r] in seenidx:
                l = max(l, seenidx[s[r]] + 1)
            
            maxi = max(maxi , r - l + 1)
            seenidx[s[r]] = r
            r += 1
        
        return maxi