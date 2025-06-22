class Solution:
    def isValid(self, s: str) -> bool:
        mapping={"}":"{",")":"(","]":"["}
        st=[]
        for i in s:
            if i in mapping.values():
                st.append(i)
            elif i in mapping.keys():
                if not st or mapping[i]!=st.pop():
                    return False
        return not st

        