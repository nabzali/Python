n = int(input("Enter number of terms in fibonacci sequence:"))
print("Fibonacci sequence for the first "+str(n)+" numbers:")
sequence = [0, 1]
for i in sequence:
    print(i)
for i in range(0, n-2):
    new = sequence[i]+sequence[i+1]
    sequence.append(new)
    print(sequence[i+2])
