def encrypt(m, k):
    m = m.upper()
    newM = ""
    for i in range(0,len(m)):
        asciiM, asciiK = ord(m[i])-64, ord(k[i])-64 #ints
        new = asciiK + asciiM + 64
        if new < 65:
            new += 26
        elif new > 90:
            new -= 26
        newM += chr(new)
    print(newM)

def decrypt(m, k):
    m = m.upper()
    newM = ""
    for i in range(0,len(m)):
        asciiM, asciiK = ord(m[i])-64, ord(k[i])-64 #ints
        new = asciiM - asciiK + 64
        if new < 65:
            new += 26
        elif new > 90:
            new -= 26
        newM += chr(new)
    print(newM)


message = str(input("Please enter a message"))
keyword = str(input("Please enter a keyword"))
option = input("Would you like to encrypt or decrypt")
while not (option == "e" or option == "d" or option == "E" or option == "D"):
    option = input("Invalid option, enter again")

while len(keyword) < len(message):
    keyword += keyword
if len(keyword) > len(message):
    x = len(keyword)-len(message)
    keyword = keyword[:-x]

if option == "e" or option == "E":
    encrypt(message, keyword)
else:
    decrypt(message, keyword)
