class Solution:
    def strStr(self, haystack: str, needle: str) -> int:


        for i in range(len(haystack)-len(needle)):
            print(i)
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1

my= Solution()
print(my.strStr("a", "a"))
