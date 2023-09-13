mydict = {}
pattern = "abba"
s = "dog cat cat fish"
s = s.split(" ")
print(s)
for i in range(0, len(pattern)):
    print(i)
    if pattern[i] not in mydict:
        mydict[pattern[i]] = s[i]
    else:
        if mydict[pattern[i]] != s[i]:
            print(False)
print(True)
