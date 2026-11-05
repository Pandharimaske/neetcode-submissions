class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps = defaultdict(list)
        for s in strs:
            temp = tuple(sorted(s))
            grps[temp].append(s)
        
        return list(grps.values())
