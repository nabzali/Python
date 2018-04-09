while True:
    try:
        n = int(input("Enter the number of triangles you would like to see\n"))
        if n < 1 or n > 10:
            print("You must enter a number between 1 and 10 inclusive. Try again.")
        else:
            break
    except ValueError:
        print("You must enter a number between 1 and 10 inclusive. Try again.")

for k in range(n, 0, -1):
    for i in range(k):
        str = " "*(k-i)
        for j in range(i):
            str = str + (" * ")
        print(str)