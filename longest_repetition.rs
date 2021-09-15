//https://www.codewars.com/kata/586d6cefbcc21eed7a001155/train/rust

use itertools::Itertools;

fn longest_repetition(s: &str) -> Option<(char, usize)> {
    match s.len() {
        0 => None,
        _ => {
            let mut max_count:usize =0;
            let mut max_key:char = 'a';
            for (k,c) in s.chars().group_by(|x| *x).into_iter().map(|(k,r)| (k,r.count())) {
                if c > max_count {
                    max_count = c;
                    max_key = k;
                }
            }
            Some((max_key,max_count))
        }
    }
}