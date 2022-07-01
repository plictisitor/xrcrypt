import math


def standardize(encoded):
    standard = [str(ord(c)) for c in encoded]
    return "-".join(standard)

def unstandardize(string):
    strange = string.split("-")
    decoded = [chr(int(c)) for c in strange]
    return "".join(decoded)

def ordsum(text):
    sum = 0
    for character in text:
        sum += ord(character)
    return sum

def helpr(num, countr = 1):
    if math.sin(num * 1337) > 0 and countr < 47:
        return abs(round(num * (num * num - 91 * helpr(15 * (4 + num % 9) - 1, countr + 1) - 1 - num % 7) * 512)) % 16
    else:
        return abs(round(num * (num * num + 91 * (15 - (4 - num % 9)) + num % 7) * 512)) % 16

def xrcrypt(text, key = "iubire", numberify = False):
    encrypted = ""
    characterid = 0

    sum_key = ordsum(key) % 1822
    text_length = len(text)

    for character in text: 
        code = ord(character)
        keycode = ord(key[characterid % len(key)])

        characterid += 1
        newcode = code

        newcode -= (9 * (keycode - 93)) % 52
        newcode += 69
        newcode += (keycode % 222)
        newcode -= (characterid % 99)
        newcode += (len(key) % 55)
        newcode += (keycode * 2 - 1) % 99
        newcode += sum_key * 3 - 9
        newcode -= (text_length + sum_key)
        newcode *= 5
        newcode *= 2 + round(keycode % 8)
        newcode += (keycode * keycode - 4) % 99
        newcode -= (keycode ** 3 - 1) % 59
        newcode += helpr(keycode * 9 - code * 7 + characterid * 5511)
        newcode += 5855 + (keycode % 118)


        encrypted += chr(int(newcode))

    if not numberify: return encrypted
    return standardize(encrypted)

def dexrcrypt(text, key = "iubire", numberify = False):
    if numberify: text = unstandardize(text)

    decrypted = ""
    characterid = 0

    sum_key = ordsum(key) % 1822
    text_length = len(text)

    for character in text:
        code = ord(character)
        keycode = ord(key[characterid % len(key)])

        newcode = code
        characterid += 1

        newcode -= 5855 + (keycode % 118)
        newcode -= helpr(keycode * 9 - code * 7 + characterid * 5511)
        newcode += (keycode ** 3 - 1) % 59
        newcode -= (keycode * keycode - 4) % 99
        newcode /= 2 + round(keycode % 8)
        newcode /= 5
        newcode += (text_length + sum_key)
        newcode -= sum_key * 3 - 9
        newcode -= (keycode * 2 - 1) % 99
        newcode -= (len(key) % 55)
        newcode += (characterid % 99)
        newcode -= (keycode % 222)
        newcode -= 69
        newcode = round(newcode)
        newcode += (9 * (keycode - 93)) % 52

        decrypted += chr(int(newcode))

    return decrypted