// https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/rust

fn solution(s: &str) -> Vec<String> {
    let mut result : Vec<String> = Vec::new();
    let input : Vec<char> = s.chars().collect();

    for i in (0..s.len()).step_by(2) {
        let mut pair = String::new();
        pair.push(input[i]);
        if i+1 == s.len() {
            pair.push('_');
        } else {
            pair.push(input[i+1]);
        }
        result.push(pair);
    }
    result
}

fn main() {
    solution("abcdef");

}