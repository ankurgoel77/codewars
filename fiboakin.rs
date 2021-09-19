// https://www.codewars.com/kata/5772382d509c65de7e000982/train/rust

use std::collections::HashMap;

fn u(n:i32, u_dict: &mut HashMap<i32,i32>) -> i32 {
    if n == 1 {
        return 1;
    } else if n == 2 {
        return 1;
    } else if u_dict.contains_key(&n) {
        return *(u_dict.get(&n).unwrap());
    } else {
        let t = u(n-u(n-1,u_dict), u_dict) + u(n-u(n-2,u_dict),u_dict);
        u_dict.insert(n,t);
        return t;
        }
}

fn length_sup_uk(n: i32, k: i32) -> i32 {
    let mut count = 0;
    let mut u_dict = HashMap::new();
    for i in 1..=n {
        if u(i, &mut u_dict) >= k {
            count += 1;
        }
    }
    count
}

fn comp(n: i32) -> i32 {
    let mut count = 0;
    let mut u_dict = HashMap::new();
    for i in 2..=n {
        if u(i,&mut u_dict) < u(i-1, &mut u_dict) {
            count += 1;
        }
    }
    count
}