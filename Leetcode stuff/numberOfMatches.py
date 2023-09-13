class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        matches = []
        

        matches.append(int(n/2))

        while matches[-1] != 1:
            matches.append(int(matches[-1]/2))
            print(matches)

        return sum(matches)


mySolution = Solution()
print(mySolution.numberOfMatches(7))

