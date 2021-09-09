// https://www.codewars.com/kata/515f51d438015969f7000013

fn pyramid(n: usize) -> Vec<Vec<u32>> {
    let mut result = Vec::new();
    for i in 1..n+1 {
        let mut row = Vec::new();
        for _j in 1..i+1 {
            row.push(1u32);
        }
        result.push(row);
    }
    result
}

fn main() {
}