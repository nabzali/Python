letterMapping = {}
index = 10
for i in range(65, 91):
    letterMapping[chr(i)] = index
    index+=1

print(letterMapping)