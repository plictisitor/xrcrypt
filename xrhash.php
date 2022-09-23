<?php

function hashxr($text = "?", $length = 64, $chars = "1234567890abcdef") {
    $text = strval($text);
    $sums = strlen($text);
    $result = "";

    for ($i = 0; $i < strlen($text); $i++) {
        $sums += ord($text[$i]) * ((round(sin(ord($text[$i]) * 73) * 1e8)) % 91);
        $sums += $length * ((round((ord($text[$i]) * 12) * 54)) % 77);
    }

    for ($i = 0; $i < $length; $i++) {
        $charfp = (ord($text[$i % strlen($text)]) * 13 - ord($text[(3 * $i - 7) % strlen($text)]) * 7) % 69;
        $charfp += round(sin($charfp - $sums * $charfp) * 1e5) % 777;
        $charfp -= round(cos($charfp + 4 * $charfp) * 1e5) % 377;
        $charfp -= round(tan($charfp * 2 + 3 * $charfp) * 1e9) % 977;
        $sums += $charfp;
        $result .= $chars[abs($charfp + $sums * 7 - 1) % strlen($chars)];
    }

    return $result;
}

// testing:
// for ($i = 0; $i < 1000; $i++) {
//     $hashed = hashxr(strval($i), 128, "   O");
//     echo "<pre>$i -> $hashed</pre>";
// }
