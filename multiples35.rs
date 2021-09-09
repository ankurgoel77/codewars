//https://www.codewars.com/kata/514b92a657cdc65150000006/train/rust

fn solution(num: i32) -> i32 {
    let mut total : i32 = 0;
      for i in 1..num {
          if (i % 3 == 0) || (i % 5 == 0) {
              total += i;
          }
      }
      total
  }