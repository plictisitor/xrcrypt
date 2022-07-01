# from hashlib import sha256
# from time import time
import math
# import random
import string

letters = string.ascii_lowercase

def hashxr(text, length = 64, chars = "1234567890abcdef"):
    sums = len(text)
    result = ""
    for i in text:
        sums += ord(i) * ((round(math.sin(ord(i)*73)*1e8))%91)
    
    sums += length * ((round(math.cos(ord(i)*12)*54))%77)
    
    for i in range(length):
        charfp = (ord(text[i%len(text)])*13 - ord(text[(3*i - 7)%len(text)])*7) % 69
        charfp += round(math.sin(charfp - sums*charfp) * 1e5)%777
        charfp -= round(math.cos(charfp + 4*charfp) * 1e5)%377
        charfp -= round(math.tan(charfp*2 + 3*charfp) * 1e9)%977
        sums += charfp
        result += chars[abs(charfp + sums*7 - 1) % len(chars)]
        
    return result

# are the same
# print(hashxr("i love you", 16, ".O"))
# print(hashxr("gaab", 16, ".O"))

# def rstring(length):
#    return ( ''.join(random.choice(letters) for i in range(length)) )
# # found = 'none'
# # countr = 0
# # while found != search_for:
# #     crackedpwd = rstring(8)
# #     found = hashxr(crackedpwd, 32, "01")
# #     if countr % 1e5 == 0:
# #         print(countr)
# #         print('tested: %s'%found)
# #     countr += 1

# # print(found)
# # print(hashxr(found))
# # print(search_for)
# # print(hashxr(search_for))
# # print("pwd: %s" % crackedpwd)

# print(search_for)
# print(crackedone)

# alfabet = "אבגדהוזחטיכךלמםנןסעפףצץקרשת       "

# intrebarea = input("explore: ")
# raspunsul = hashxr(intrebarea, 1600, alfabet)
# while True:
#     print(raspunsul)
#     input()
#     raspunsul = hashxr(raspunsul, 1600, alfabet)