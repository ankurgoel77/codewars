// https://www.codewars.com/kata/5d98b6b38b0f6c001a461198/train/rust

fn code(s: &str) -> String {
    let mut result = String::new();
    for c in s.chars() {
        let digit = c.to_digit(10).unwrap();
        let binary = format!("{:b}",digit);
        let k = binary.len();
        for _ in 0..k-1 {
            result.push('0');
        }
        result.push('1');
        result.push_str(&binary);
    }
    result
}



fn decode(s: &str) -> String {
    let mut current = 0;
    let mut i = s.find("1");
    let mut result = String::new();

    while i != None {
        let k = i.unwrap() + 1;
        current += i.unwrap() + 1;
        result += match &s[current..current+k] {
            "0" => "0",
            "1" => "1",
            "10" => "2",
            "11" => "3",
            "100" => "4",
            "101" => "5",
            "110" => "6",
            "111" => "7",
            "1000" => "8",
            "1001" => "9",
            _ => "0",
        };
        current += k;
        i = (s[current..]).find("1")
    }
    result
}
