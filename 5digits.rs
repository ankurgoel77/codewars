// https://www.codewars.com/kata/51675d17e0c1bed195000001/train/rust

use std::str::FromStr;

fn largest_five_digit_number(num: &str) -> u32 {
    let mut max = 0;
    if num.len() <= 5 {
        max = u32::from_str(&num).unwrap();
    } else {
        for counter in 0..(num.len()-4) {
            let test = u32::from_str(&num[counter..counter+5]).unwrap();
            if test > max {
                max = test;
            }
        }
    }
    max
}

fn main() {
    println!("{}", largest_five_digit_number(&"1234567890"))
}