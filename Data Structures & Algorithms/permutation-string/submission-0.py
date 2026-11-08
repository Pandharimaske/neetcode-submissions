class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if m < n: return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        for c in s1:
            ind = ord(c) - ord('a')
            freq1[ind] += 1
        
        l , r = 0 , 0
        while r < m:
            freq2[ord(s2[r]) - ord('a')] += 1
            while r - l + 1 > n:
                freq2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            if r - l + 1 == n:
                isper = True
                for i in range(26):
                    if freq1[i] != freq2[i]:
                        isper = False
                        break
                
                if isper: return True
            
            r += 1
        
        return False


        
