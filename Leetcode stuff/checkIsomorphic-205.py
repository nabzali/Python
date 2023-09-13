class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #for letter in s, if not in dict, add. if in dict, check correct corresponding letter is stored
        mydict = {}
        for i in range(len(s)):
            if s[i] not in mydict and t[i] not in mydict.values():
                mydict[s[i]] = t[i]
            if s[i] in mydict and mydict[s[i]] != t[i]:
                return False
            if t[i] in mydict.values() and s[i] not in mydict:
                return False
                    
        return True
        

mySol = Solution()
print(mySol.isIsomorphic("paper", "title")) #expect true
print(mySol.isIsomorphic("foo", "bar")) #expect false
print(mySol.isIsomorphic("badc", "baba")) #expect false
