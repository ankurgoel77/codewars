// https://www.codewars.com/kata/59f44c7bd4b36946fd000052/train/rust

fn hist(s: &str) -> String {
    let mut errors = [0;4];  // array of count 4 letters u, w, x , z
    let letters = ['u','w','x','z'];
    for c in s.chars(){
        match c {
            'u' => errors[0] += 1,
            'w' => errors[1] += 1,
            'x' => errors[2] += 1,
            'z' => errors[3] += 1,
            _ => (),
        }
    }
    
    let mut result : Vec<String> = Vec::with_capacity(4);
    
    for i in 0..4 {
        if errors[i] > 0 {
            let mut stars = String::new();
            for _ in 0..errors[i] {
                stars.push('*');
            }
            result.push(format!("{}  {}     {}",letters[i],errors[i],stars));
        }
    }
    result.join("\r")
}