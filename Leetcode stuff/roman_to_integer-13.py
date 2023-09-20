class Solution:
    def romanToInt(self, s: str) -> int:
        # create Dictionary for numeral values
        romanDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        # work backwards: reverse the string and subtract value from total if its lower than val before it. 
        # otherwise add each value to a total
        reverseS = s[::-1]
        total = 0
        for i in range(len(s)):
            if i > 0 and romanDict[reverseS[i]] < romanDict[reverseS[i-1]]:
                total -= romanDict[reverseS[i]]
            else:
                total += romanDict[reverseS[i]]


        return total