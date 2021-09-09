// https://www.codewars.com/kata/58223370aef9fc03fd000071

fn dashatize(n: i64) -> String {
    let chars : Vec<char> = n.abs().to_string().chars().collect();
    let mut dash = String::new();
    for i in 0..(chars.len()-1) {
        if isOdd(chars[i]) || isOdd(chars[i+1]) {
            dash.push_str(&format!("{}-",chars[i]))
        } else {
            dash.push(chars[i])
        }
    }
    dash.push(chars[chars.len()-1]);
    dash
}

fn isOdd(c: char) -> bool {
    match c {
        '1'|'3'|'5'|'7'|'9' => return true,
        _ => return false,
    }
}