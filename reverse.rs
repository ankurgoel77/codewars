// https://www.codewars.com/kata/5259b20d6021e9e14c0010d4

fn reverse_words(str: &str) -> String {
    str.split(" ").map(|x| x.chars().rev().collect::<String>()).collect::<Vec<String>>().join(" ")
}