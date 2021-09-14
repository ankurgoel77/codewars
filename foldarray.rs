// https://www.codewars.com/kata/57ea70aa5500adfe8a000110/train/rust

fn fold_array(arr: &[i32], runs: usize) -> Vec<i32> {
    fn fold_even (input: Vec<i32>) -> Vec<i32> {
        let mut result: Vec<i32> = Vec::with_capacity(input.len() / 2);
        for i in 0..(input.len()/2) {
            result.push(input[i] + input[input.len()-i-1])
        }
        result
    }

    fn fold_odd (input: Vec<i32>) -> Vec<i32> {
        let mut result: Vec<i32> = Vec::with_capacity(input.len() / 2 + 1);
        for i in 0..(input.len()/2) {
            result.push(input[i] + input[input.len()-i-1])
        }
        result.push(input[input.len()/2]);
        result
    }

    let mut result:Vec<i32> = Vec::from(arr);
    for _ in 0..runs {
        match result.len() % 2 {
            0 => result = fold_even(result),
            _ => result = fold_odd(result),
        }
    }
    result
}