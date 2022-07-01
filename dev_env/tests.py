import traiancrypt

xrcrypt = traiancrypt.xrcrypt
dexrcrypt = traiancrypt.dexrcrypt

testme = input("Enter text to encrypt: ")

print("test1: " + str(dexrcrypt(xrcrypt(testme, "A"), "A") == testme))
print("test2: " + str(dexrcrypt(xrcrypt(testme, "B"), "B") == testme))
print("test3: " + str(dexrcrypt(xrcrypt(testme, "C"), "C") == testme))
print("test4: " + str(dexrcrypt(xrcrypt(testme, "D"), "D") == testme))
print("test5: " + str(dexrcrypt(xrcrypt(testme, "E"), "E") == testme))
print("test6: " + str(dexrcrypt(xrcrypt(testme, "F"), "F") == testme))
print("test7: " + str(dexrcrypt(xrcrypt(testme, "G"), "G") == testme))
print("test8: " + str(dexrcrypt(xrcrypt(testme, "H"), "H") == testme))
print("test9: " + str(dexrcrypt(xrcrypt(testme, "I"), "I") == testme))
print("test10: " + str(dexrcrypt(xrcrypt(testme, "J"), "J") == testme))
print("test11: " + str(dexrcrypt(xrcrypt(testme, "K"), "K") == testme))
print("test12: " + str(dexrcrypt(xrcrypt(testme, "L"), "L") == testme))
print("test13: " + str(dexrcrypt(xrcrypt(testme, "M"), "M") == testme))
print("test14: " + str(dexrcrypt(xrcrypt(testme, "N"), "N") == testme))
print("test15: " + str(dexrcrypt(xrcrypt(testme, "O"), "O") == testme))
print("test16: " + str(dexrcrypt(xrcrypt(testme, "P"), "P") == testme))

print(xrcrypt("Hello World!", "lets_all_love_lain"))
print(dexrcrypt("䐀䵡䡖䂟沸⹤䔎䟀沋䜪挰儩", "lets_all_love_lain"))