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
    num += 1
    if math.sin(num * 1337) > 0 and countr < 47:
        return (helpr(9 * (3 + num), countr + 4) + abs(round(num - (num - 19 * helpr(15 * (4 + num % 9) - 1, countr + 1) - 1 - num % 7)))) % 16
    else:
        return abs(round(num - (num * num + 19 * (15 - (4 - num % 9)) + num % 7) * 3)) % 55

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

        newcode += 69
        # print("enc += 69: " + str(newcode))
        newcode += (keycode % 222)
        # print("enc += (keycode % 222): " + str(newcode))
        newcode -= (characterid % 99)
        # print("enc -= (characterid % 99): " + str(newcode))
        newcode += (len(key) % 55)
        # print("enc += (len(key) % 55): " + str(newcode))
        newcode += (keycode * 2 - 1) % 99
        # print("enc += (keycode * 2 - 1) % 99: " + str(newcode))
        newcode += sum_key * 3 - 9
        # print("enc += sum_key * 3 - 9: " + str(newcode))
        newcode -= (text_length + sum_key)
        # print("enc -= (text_length + sum_key): " + str(newcode))
        newcode += 5 * (keycode % 3)
        # print("enc += 5 * (keycode % 3): " + str(newcode))
        newcode -= 7 + round(keycode % 8)
        # print("enc -= 7 + round(keycode % 8): " + str(newcode))
        newcode += (keycode * keycode - 4) % 99
        # print("enc += (keycode * keycode - 4) % 99: " + str(newcode))
        newcode -= (keycode ** 3 - 1) % 59
        # print("enc -= (keycode ** 3 - 1) % 59: " + str(newcode))
        newcode += helpr(keycode * 9 - text_length * 7 + characterid * 5511)
        # print("enc += helpr(keycode * 9 - code * 7 + characterid * 5511): " + str(newcode))
        newcode += 1 + (keycode % 118)
        # print("enc += 1 + (keycode % 118): " + str(newcode))

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

        newcode -= 1 + (keycode % 118)
        # print("dec -= 1 + (keycode % 118): " + str(newcode))
        newcode -= helpr(keycode * 9 - text_length * 7 + characterid * 5511)
        # print("dec -= helpr(keycode * 9 - code * 7 + characterid * 5511): " + str(newcode))
        newcode += (keycode ** 3 - 1) % 59
        # print("dec += (keycode ** 3 - 1) % 59: " + str(newcode))
        newcode -= (keycode * keycode - 4) % 99
        # print("dec -= (keycode * keycode - 4) % 99: " + str(newcode))
        newcode += 7 + round(keycode % 8)
        # print("dec += 7 + round(keycode % 8): " + str(newcode))
        newcode -= 5 * (keycode % 3)
        # print("dec -= 5 * (keycode % 3): " + str(newcode))
        newcode += (text_length + sum_key)
        # print("dec += (text_length + sum_key): " + str(newcode))
        newcode -= sum_key * 3 - 9
        # print("dec -= sum_key * 3 - 9: " + str(newcode))
        newcode -= (keycode * 2 - 1) % 99
        # print("dec -= (keycode * 2 - 1) % 99: " + str(newcode))
        newcode -= (len(key) % 55)
        # print("dec -= (len(key) % 55): " + str(newcode))
        newcode += (characterid % 99)
        # print("dec += (characterid % 99): " + str(newcode))
        newcode -= (keycode % 222)
        # print("dec -= (keycode % 222): " + str(newcode))
        newcode -= 69
        # print("dec -= 69: " + str(newcode))

        decrypted += chr(int(newcode))

    return decrypted

# encoded = xrcrypt("Hello world")
# print(encoded)
# print(dexrcrypt(encoded))