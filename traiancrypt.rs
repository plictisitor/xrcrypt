fn xrcrypt(line: String, key: String) -> String {
    let mut counter = 0;
    let mut newstring = Vec::new();
    
    for char in line.chars() {
        let code = char as u32;
        counter += 1;
        let keycode = key.chars().nth(counter%(key.len())).unwrap() as u32;
        let mut newcode = code;
        newcode += 69;
        newcode += keycode % 222 as u32;
        newcode += (key.len() % 55) as u32;
        newcode += (keycode * 2 - 1) % 99;
        newcode += 5 * (keycode % 3);
        newcode -= 7 + (keycode % 8);
        newcode += (keycode * keycode - 4) % 99;
        newcode -= (keycode.pow(3) - 1) % 59;
        newcode += 1 + (keycode % 118);
        newstring.push(char::from_u32(newcode).unwrap());
    }
    
    let result1 = newstring.iter().collect::<String>();
    return result1;
}

fn dexrcrypt(line: String, key: String) -> String {
    let mut counter = 0;
    let mut newstring = Vec::new();
    
    for char in line.chars() {
        let code = char as u32;
        counter += 1;
        let keycode = key.chars().nth(counter%(key.len())).unwrap() as u32;
        let mut newcode = code;
        newcode -= 1 + (keycode % 118);
        newcode += (keycode.pow(3) - 1) % 59;
        newcode -= (keycode * keycode - 4) % 99;
        newcode += 7 + (keycode % 8);
        newcode -= 5 * (keycode % 3);
        newcode -= (keycode * 2 - 1) % 99;
        newcode -= (key.len() % 55) as u32;
        newcode -= keycode % 222 as u32;
        newcode -= 69;
        newstring.push(char::from_u32(newcode).unwrap());
    }
    
    let result1 = newstring.iter().collect::<String>();
    return result1;
}

// fn main() {
//     let line = String::from("secret text");
//     let key = String::from("meow");
    
//     let encrypted = xrcrypt(line, key.clone());
    
//     println!("encrypted: {}", encrypted);
//     println!("decrypted: {}", dexrcrypt(encrypted, key.clone()));
// }