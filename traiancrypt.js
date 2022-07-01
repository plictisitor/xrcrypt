function standardize(encoded) {
    standard = []
    for (character of encoded) {
        standard.push(ord(character))
    }
    return standard.join("-")
}

function unstandardize(string) {
    strange = string.split("-")
    decoded = ""
    for (character of strange) {
        decoded += chr(parseInt(character))
    }
    return decoded
}

function round(number) {
    return Math.round(number)
}

function chr(code) {
    return String.fromCharCode(code)
}

function len(text) {
    return text.toString().length
}

function ord(character) {
    return character.charCodeAt(0)
}

function ordsum(text) {
    sum = 0
    for (character of text) {
        sum += ord(character)
    }
    return sum
}

function abs(number) {
    if (number < 0) return -number
    return number
}

function helpr(num, countr = 1) {
    if (Math.sin(num * 1337) > 0 && countr < 47) {
        return abs(round(num * (num * num - 91 * helpr(15 * (4 + num % 9) - 1, countr + 1) - 1 - num % 7) * 512)) % 16
    } else {
        return abs(round(num * (num * num + 91 * (15 - (4 - num % 9)) + num % 7) * 512)) % 16
    }
}


function xrcrypt(text, key = "iubire", numberify = false) {
    encrypted = ""
    characterid = 0

    sum_key = ordsum(key) % 1822;
    text_length = len(text);

    for (character of text) {

        code = ord(character)
        keycode = ord(key[characterid % len(key)])

        characterid += 1
        newcode = code


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



        encrypted += chr(newcode)
    }

    if (!numberify) return encrypted
    return standardize(encrypted);
}

function dexrcrypt(text, key = "iubire", numberify = false) {
    if (numberify) text = unstandardize(text)

    decrypted = ""
    characterid = 0

    sum_key = ordsum(key) % 1822;
    text_length = len(text);

    for (character of text) {

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



        newcode = Math.round(newcode)
        decrypted += chr(newcode)
    }

    return decrypted;
}