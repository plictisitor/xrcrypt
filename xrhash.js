function ord(character) {
    // if its undefined, return 0
    if (character === undefined) return 0;
    return character.charCodeAt(0)
}

function round(number) {
    return Math.round(number)
}

function hashxr(text, length = 64, chars = "1234567890abcdef") {
    var sums = text.length;
    var result = "";

    for (var i = 0; i < text.length; i++) {
        sums += ord(text[i]) * ((round(Math.sin(ord(text[i]) * 73) * 1e8)) % 91);
    }

    sums += length * ((round(Math.cos(ord(text[i]) * 12) * 54)) % 77);

    for (var i = 0; i < length; i++) {
        var charfp = (ord(text[i % text.length]) * 13 - ord(text[(3 * i - 7) % text.length]) * 7) % 69;
        charfp += round(Math.sin(charfp - sums * charfp) * 1e5) % 777;
        charfp -= round(Math.cos(charfp + 4 * charfp) * 1e5) % 377;
        charfp -= round(Math.tan(charfp * 2 + 3 * charfp) * 1e9) % 977;
        sums += charfp;
        result += chars[Math.abs(charfp + sums * 7 - 1) % chars.length];
    }

    return result;
}

// console.log(hashxr("traian"));
// console.log(hashxr("xraian"));