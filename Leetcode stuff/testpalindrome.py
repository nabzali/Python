def isPalindrome(s):
    cleanString = ""
    for c in s:
        if c.isalnum():
            cleanString += c
    
    if cleanString[::-1] == cleanString:
        return True
    return False

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("amanaplanacanalpanama"))
print(isPalindrome("palindrome"))


    

