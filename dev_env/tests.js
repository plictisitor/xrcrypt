var fs = require('fs');

// file is included here:
eval(fs.readFileSync('../traiancrypt.js').toString());

testme = "salutare"

console.log("test1: " + (dexrcrypt(xrcrypt(testme, "A"), "A") == testme).toString())
console.log("test2: " + (dexrcrypt(xrcrypt(testme, "B"), "B") == testme).toString())
console.log("test3: " + (dexrcrypt(xrcrypt(testme, "C"), "C") == testme).toString())
console.log("test4: " + (dexrcrypt(xrcrypt(testme, "D"), "D") == testme).toString())
console.log("test5: " + (dexrcrypt(xrcrypt(testme, "E"), "E") == testme).toString())
console.log("test6: " + (dexrcrypt(xrcrypt(testme, "F"), "F") == testme).toString())
console.log("test7: " + (dexrcrypt(xrcrypt(testme, "G"), "G") == testme).toString())
console.log("test8: " + (dexrcrypt(xrcrypt(testme, "H"), "H") == testme).toString())
console.log("test9: " + (dexrcrypt(xrcrypt(testme, "I"), "I") == testme).toString())
console.log("test10: " + (dexrcrypt(xrcrypt(testme, "J"), "J") == testme).toString())
console.log("test11: " + (dexrcrypt(xrcrypt(testme, "K"), "K") == testme).toString())
console.log("test12: " + (dexrcrypt(xrcrypt(testme, "L"), "L") == testme).toString())
console.log("test13: " + (dexrcrypt(xrcrypt(testme, "M"), "M") == testme).toString())
console.log("test14: " + (dexrcrypt(xrcrypt(testme, "N"), "N") == testme).toString())
console.log("test15: " + (dexrcrypt(xrcrypt(testme, "O"), "O") == testme).toString())
console.log("test16: " + (dexrcrypt(xrcrypt(testme, "P"), "P") == testme).toString())
console.log("test17: " + (dexrcrypt(xrcrypt(testme, "Q"), "Q") == testme).toString())
console.log("test18: " + (dexrcrypt(xrcrypt(testme, "R"), "R") == testme).toString())
console.log("test19: " + (dexrcrypt(xrcrypt(testme, "S"), "S") == testme).toString())
console.log("test20: " + (dexrcrypt(xrcrypt(testme, "T"), "T") == testme).toString())
console.log("test21: " + (dexrcrypt(xrcrypt(testme, "U"), "U") == testme).toString())
console.log("test22: " + (dexrcrypt(xrcrypt(testme, "V"), "V") == testme).toString())
console.log("test23: " + (dexrcrypt(xrcrypt(testme, "W"), "W") == testme).toString())
console.log("test24: " + (dexrcrypt(xrcrypt(testme, "X"), "X") == testme).toString())
console.log("test25: " + (dexrcrypt(xrcrypt(testme, "Y"), "Y") == testme).toString())
console.log("test26: " + (dexrcrypt(xrcrypt(testme, "Z"), "Z") == testme).toString())

// they will work 100%
console.log(xrcrypt("Hello world!"))
console.log(xrcrypt("Hello World!", "lets_all_love_lain"))
console.log(dexrcrypt("䞢倝乐䒹濢む䢰䭢澵䫌搾发", "lets_all_love_lain"))