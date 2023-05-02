# xrcrypt

### LIVE EXAMPLE: [tra1an.com/xrcrypt/](https://tra1an.com/xrcrypt/)

### usage

xrcryption javascript:
```js
> xrcrypt("secret",'key')
"瑌钜倽珨鐳儏"
> xrcrypt("secret",'key',true)
"29772-38044-20541-29672-37939-20751"
> dexrcrypt("瑌钜倽珨鐳儏",'key')
"secret"
> dexrcrypt("29772-38044-20541-29672-37939-20751",'key', true)
"secret" 
```
xrcryption python:
```py
>> xrcrypt("secret") 
'狾\uef9f鍞狂迻\ue8d4'
>>> xrcrypt("secret",'key') 
'爦釠䶩燂酷乻'
>>> xrcrypt("secret",'key',True)  
'29222-37344-19881-29122-37239-20091'
>>> dexrcrypt("爦釠䶩燂酷乻",'key')                             
'secret'
>>> dexrcrypt("29222-37344-19881-29122-37239-20091",'key',True) 
'secret'
```

hashxr javascript:
```js
> hashxr("i love you")
"01a6db0908d2a16c23c4b3447b6b83e4eac606c61d955f3b937fe0afd5cf08e4"
> hashxr("i hate you")
"9ee7c65266b27c2eb9c52bb17bf11d64f86aaef70786998afbae960b80bd2f68"
> hashxr("c", 128, "12345678990ABCDEFGHIJKL")
"2D3GI2CB47I9H81J6E46A44AGB7C85GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG"
```
hashxr python:
```py
>>> hashxr("i love you")
'008acb34a6e755ca5b49ff2ffdadd0ad8363f9b2b424c80f6dd2b0349eda10b6'
>>> hashxr("i hate you") 
'e2da7d077b0aac035517ee56b9c5e430df0be0c9d5abd4ff246d181b70849c58'
>>> hashxr("uuuuuuuuuuuuu", 128, "XR0") 
'RRRR0RRXXX0RX0RXRRRRXXRRRRRX0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
```

### notes

- `algorithms are really slow`. lmao bro i know thats a feature not a bug. if it was fast, hashes could be cracked really easy bhaahhhaha
- ~~`some keys distort the text after decryption`. well this not my problem go find a key that works lol~~ fixed. now its actually stable
- ~~`python functions return different results than js functions`. well yeah idc this is not a bug because i didnt want them to be the same lol~~ fixed
- `results do not look pseudorandom! hashxr("qqqqqqqqqqqq") is 'f800000000000000000000000000000000000000000000000000000000000000'` yea i know that is also a feature, not a bug. it will confuse hackers really bad if they get to your db data it will be funny

### how does the encryption algorithm work? what are those numbers

- idk 💀💀

### how does the hashing algorithm work? what are those numbers

- don't ask me. i was not awake when i made it. it's channeled from the higher self. initially, it was not a hashing algorithm. you were supposed to ask a question and the hash of that question is the answer but you need to interpret it somehow. if you press randomly on a keyboard for 50 years you will probably write your full name, you kno what im sayin?? if you look into xrhash.py you can still see the original purpose:
```py
# intrebarea = input("explore: ")
# raspunsul = hashxr(intrebarea, 1600, alfabet)
# while True:
#     print(raspunsul)
#     input()
#     raspunsul = hashxr(raspunsul, 1600, alfabet)
```

### is this project a joke??

- yes and no. it's not that secure but sometimes it's useful. i used it to text my friends secret stuff
- the hashing function is not "hashing" but the results are similar to a hexdigest to yeah
- i published in on github just so i can use it in the future it's really fun lol








𐋁૦ⴴ૦𐋁૦ⴴ૦𐋁૦ⴴ૦𐋁૦ⴴ૦𐋁૦ⴴ૦𐋁૦ⴴ૦𐋁૦ⴴ૦𐋁૦ⴴ૦𐋁૦ⴴ૦𐋁૦ⴴ૦𐋁૦ⴴ૦𐋁૦ⴴ૦𐋁૦ⴴ૦𐋁૦ⴴ૦𐋁૦ⴴ૦𐋁૦ⴴ૦𐋁૦ⴴ૦𐋁૦ⴴ૦𐋁૦ⴴ૦𐋁૦ⴴ૦𐋁૦ⴴ૦𐋁૦ⴴ૦𐋁૦ⴴ
