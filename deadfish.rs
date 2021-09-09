// https://www.codewars.com/kata/51e0007c1f9378fa810002a9/train/rust

fn parse(code: &str) -> Vec<i32> {
    let mut value : i32 = 0;
    let mut output = Vec::<i32>::new();
    
    for c in code.chars() {
        match c {
            'i' => value += 1,
            'd' => value -= 1,
            's' => value *= value,
            'o' => output.push(value),
            _ => (),
        }
    }
    output
}