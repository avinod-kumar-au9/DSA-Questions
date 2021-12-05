def lengthOfLongestSubstring(self, s: str) -> int:
        l=len(s)
        if(list(set(s))==l):
            return l
        c=0
        a=[]
        for i in range(0,l):
            if(s[i] not in a):
                a.append(s[i])
                l=len(a)
            else:
                while(s[i] in a):
                    a.pop(0)
                a.append(s[i])
                l=len(a)
            if(l>c):
                c=l
        return c


self=None
print(lengthOfLongestSubstring(self,"abcbcasc"))

