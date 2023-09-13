class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def div4(x):
            print(x)
            if (x == 4.0):
                return True
            if (x < 4):
                return False
            return div4(x/4)
        div4(n)

myclass = Solution()
print(myclass.isPowerOfFour(16))
