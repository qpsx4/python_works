import string


keys = {x: chr(y) for x, y in zip(string.ascii_letters + " ",
                                  range(0x4e10, 0x4e80))}

message = list(input("Enter a message: "))

for symbol in range(len(message)):
    for key in keys:
        if message[symbol] == key:
            message[symbol] = keys[key]
        elif message[symbol] == keys[key]:
            message[symbol] = key

print("Encrypted/decrypted message: ", *message, sep="")
