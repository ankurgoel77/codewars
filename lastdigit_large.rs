//https://www.codewars.com/kata/5511b2f550906349a70004e1/solutions/rust

fn last_digit(str1: &str, str2: &str) -> i32 {
    if str2 == "0" {
        return 1;
    }

    let dict = [
        [0,0,0,0],
        [1,1,1,1],
        [6,2,4,8],
        [1,3,9,7],
        [6,4,6,4],
        [5,5,5,5],
        [6,6,6,6],
        [1,7,9,3],
        [6,8,4,2],
        [1,9,1,9],
    ];

    let v1 = str1.chars().collect::<Vec<char>>();
    let v2 = str2.chars().collect::<Vec<char>>();
    
    let i = v1[v1.len()-1].to_digit(10).unwrap();
    let mut j = v2[v2.len()-1].to_digit(10).unwrap();
    if v2.len() > 1 {
        j += 10 * v2[v2.len()-2].to_digit(10).unwrap();
    }
    j %= 4;

    dict[i as usize][j as usize]

  }