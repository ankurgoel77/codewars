// https://www.codewars.com/kata/6135e4f40cffda0007ce356b/train/rust


// start and end pos must both sum to even or to odd
// 2 moves can get you anywhere on the board

fn bishop(start_pos: &str, end_pos: &str, num_moves: u8) -> bool {
    let start_col = start_pos.chars().nth(0).unwrap().to_digit(18).unwrap()-10;
    let start_row = start_pos.chars().nth(1).unwrap().to_digit(18).unwrap();
    let end_col = end_pos.chars().nth(0).unwrap().to_digit(18).unwrap()-10;
    let end_row = end_pos.chars().nth(1).unwrap().to_digit(18).unwrap();

    if (start_col + start_row) % 2 != (end_col + end_row) % 2 {
        return false;
    }

    match num_moves {
        0 => start_pos == end_pos,
        1 => (start_row.max(end_row)-start_row.min(end_row) ) == (start_col.max(end_col)-start_col.min(end_col) ) ,
        _ =>  true,
    }
}
