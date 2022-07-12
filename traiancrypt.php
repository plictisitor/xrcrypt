<?php

function len($text) {
    if (is_array($text)) {
        return count($text);
    } else {
        return strlen($text);
    }
    return strlen($text);
}

function ordsum($text) {
    $sum = 0;
    foreach (str_split($text) as $char) {
        $sum += ord($char);
    }
    return $sum;
}

function helpr($num, $countr = 1) {
    $num += 1;
    if (sin($num * 1337) > 0 && $countr < 47) {
        return helpr(9 * (3 + $num), $countr + 4) + abs(round($num - ($num - 19 * helpr(15 * (4 + $num % 9) - 1, $countr + 1) - 1 - $num % 7))) % 16;
    } else {
        return abs(round($num - ($num * $num + 19 * (15 - (4 - $num % 9)) + $num % 7) * 3)) % 55;
    }
}


function xrcrypt($text, $key = "iubire") {
    $encrypted = "";
    $characterid = 0;

    $sum_key = ordsum($key) % 1822;
    $text_length = len($text);

    foreach (str_split($text) as $character) {
        $code = ord($character);
        $keycode = ord($key[$characterid % len($key)]);

        $characterid += 1;
        $newcode = $code;


        $newcode += 69;
        $newcode += ($keycode % 222);
        $newcode -= ($characterid % 99);
        $newcode += (len($key) % 55);
        $newcode += ($keycode * 2 - 1) % 99;
        $newcode += $sum_key * 3 - 9;
        $newcode -= ($text_length + $sum_key);
        $newcode += 5 * ($keycode % 3);
        $newcode -= 7 + round($keycode % 8);
        $newcode += ($keycode * $keycode - 4) % 99;
        $newcode -= ($keycode ** 3 - 1) % 59;
        $newcode += helpr($keycode * 9 - $text_length * 7 + $characterid * 5511);
        $newcode += 1 + ($keycode % 118);

        $encrypted .= chr($newcode);
    }

    return utf8_encode($encrypted);
}

function dexrcrypt($text, $key = "iubire") {
    $text = utf8_decode($text);

    $decrypted = "";
    $characterid = 0;

    $sum_key = ordsum($key) % 1822;
    $text_length = len($text);

    foreach (str_split($text) as $character) {
        $code = ord($character);
        $keycode = ord($key[$characterid % len($key)]);

        $newcode = $code;
        $characterid += 1;

        $newcode -= 1 + ($keycode % 118);
        $newcode -= helpr($keycode * 9 - $text_length * 7 + $characterid * 5511);
        $newcode += ($keycode ** 3 - 1) % 59;
        $newcode -= ($keycode * $keycode - 4) % 99;
        $newcode += 7 + round($keycode % 8);
        $newcode -= 5 * ($keycode % 3);
        $newcode += ($text_length + $sum_key);
        $newcode -= $sum_key * 3 - 9;
        $newcode -= ($keycode * 2 - 1) % 99;
        $newcode -= (len($key) % 55);
        $newcode += ($characterid % 99);
        $newcode -= ($keycode % 222);
        $newcode -= 69;

        $newcode = round($newcode);
        $decrypted .= chr($newcode);
    }

    return $decrypted;
}


// for ($i = 0; $i < 1000; $i++) {
//     $helpr = helpr($i * 5000);
//     echo "<pre>$i -> $helpr</pre>";
// }

// echo xrcrypt("Hello World!");
// echo "<br>";
// echo dexrcrypt(xrcrypt("Hello World!"));