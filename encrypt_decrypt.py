import string

def encrypt(key, message):
    message = message.translate(str.maketrans('','', string.punctuation)).translate(str.maketrans('','', '1234567890 ')).lower()
    cipher = ""
    for char in message:
        if ord(char) + key > 122:
            cipher += chr(ord(char) + key - 26)
        else:
            cipher += chr(ord(char) + key)
    return cipher


def decrypt(key, cipher):
    message = ""
    for char in cipher:
        if ord(char) - key < 97:
            message += chr(ord(char) - key + 26)
        else:
            message += chr(ord(char) - key)
    return message


if __name__ == '__main__':
    choice = input("[enc/dec]: ")

    while choice != "enc" and choice != "dec":
        choice = input("\nPlease choose an action [enc/dec]: ")

    if choice == "enc":
        text = input("\nPlain text: ")
        key = input("\nKey [0-25]: ")
        print("\nCipher text: " + encrypt(int(key), text))
    elif choice == "dec":
        text = input("\nCipher text: ")
        key = input("\nKey: ")
        print("\nPlain text: " + decrypt(int(key), text))












