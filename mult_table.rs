// https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/rust

fn multiplication_table(len: usize) -> Vec<Vec<usize>> {
    let mut table = vec![vec![0;len];len];
    for i in 0..len {
        for j in 0..len {
            table[i][j] = (i+1)* (j+1);
        }
    }
    table
}