# Nabeel Ali | Fizz Buzz

fizz = int(input("What is your fizz?"))
buzz = int(input("What is your buzz?"))
limit = int(input("What is your limit>"))
for i in range(1, limit):
    if i % fizz == 0 and i % buzz == 0:
        print("FIZZ BUZZ")
    elif i % fizz == 0:
        print("FIZZ")
    elif i % buzz == 0:
        print("BUZZ")
    else:
        print(i)
