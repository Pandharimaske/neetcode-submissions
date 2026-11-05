class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps = dict()
        for s in strs:
            temp = list(s)
            temp.sort()
            temp = ("").join(temp)
            if temp not in grps:
                grps[temp] = []
            grps[temp].append(s)

        ans = []
        
        for k , grp in grps.items():
            ans.append(grp)
        
        return ans
