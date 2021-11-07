def encrypt(text, shift):
    sText = ""

    for i in range(len(text)):

        tmp = text[i]
        if tmp.isalpha():

            if ord(tmp) >= 65 and ord(tmp) <= 90:
                tmp = chr((ord(tmp) + shift) % 91)
                if (ord(tmp) < 65):
                    tmp = chr(ord(tmp) + 65)
                sText += str(tmp)

            elif ord(tmp) >= 97 and ord(tmp) <= 122:
                tmp = chr((ord(tmp) + shift) % 123)
                if (ord(tmp) < 97):
                    tmp = chr(ord(tmp) + 97)
                sText += str(tmp)
        else:
            sText += str(tmp)

    print(len(text))
    print(len(sText))

    return sText

def desencrypt(text, shift):
    sText = ""

    for i in range(len(text)):

        tmp = text[i]
        if tmp.isalpha():

            if ord(tmp) >= 65 and ord(tmp) <= 90:
                tmp = chr((ord(tmp) - shift))
                if (ord(tmp) < 65):
                    tmp = chr(ord(tmp) + 26)
                sText += str(tmp)

            elif ord(tmp) >= 97 and ord(tmp) <= 122:
                tmp = chr((ord(tmp) - shift))
                if (ord(tmp) < 97):
                    tmp = chr(ord(tmp) + 26)
                sText += str(tmp)
        else:
            sText += str(tmp)

    print(len(text))
    print(len(sText))

    return sText

print(encrypt("Zapatilla", 3))
print(desencrypt("Cdsdwlood", 3))
