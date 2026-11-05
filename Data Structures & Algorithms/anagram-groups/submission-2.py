class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps = defaultdict(list)
        for s in strs:
            # temp = tuple(sorted(s))
            # grps[temp].append(s)
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            grps[tuple(count)].append(s)
        
        return list(grps.values())
