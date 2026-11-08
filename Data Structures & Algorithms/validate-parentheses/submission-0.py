class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        st = []
        for c in s:
            if c in [')' , ']' , '}']:
                if len(st) == 0 or (c == ')' and st[-1] != '(') or (c == '}' and st[-1] != '{') or (c == ']' and st[-1] != '['):
                    return False
                else:
                    st.pop()
            
            else:
                st.append(c)
        
        if len(st) != 0:
            return False
        return True