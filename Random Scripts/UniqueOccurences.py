arr = [1, 1, 2]

dic = {}
seen = []
for num in arr:
    if num not in seen:
        seen.append(num)
        dic[num] = arr.count(num)

for key, value in dic.items():
    if dic.items().count(value) > 1:
        print(False)
print(True)

