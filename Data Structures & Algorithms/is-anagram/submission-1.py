class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m: return False

        freq = dict()
        for c in s:
            freq[c] = 1 + freq.get(c , 0)
        
        for c in t:
            if c not in freq or freq[c] == 0:
                return False
            freq[c] -= 1
        
        return True