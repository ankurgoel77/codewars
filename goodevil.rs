// https://www.codewars.com/kata/52761ee4cffbc69732000738/train/rust

fn good_vs_evil(good: &str, evil: &str) -> String {

    let good_vec : Vec<i32> = good.split(" ").map(|letter| {letter.parse::<i32>().unwrap()}).collect();
    let evil_vec : Vec<i32> = evil.split(" ").map(|letter| {letter.parse::<i32>().unwrap()}).collect();

    let good_score = 1*good_vec[0] + 2*good_vec[1] + 3*good_vec[2] + 3*good_vec[3] + 4*good_vec[4] + 10*good_vec[5];
    let evil_score  = 1*evil_vec[0] + 2*evil_vec[1] + 2*evil_vec[2] + 2*evil_vec[3] + 3*evil_vec[4] + 5*evil_vec[5]+ 10*evil_vec[6];

    if good_score < evil_score {
        return String::from("Battle Result: Evil eradicates all trace of Good");
    } else if good_score > evil_score {
        return String::from("Battle Result: Good triumphs over Evil");
    } else {
        return String::from("Battle Result: No victor on this battle field");
    }

  }

fn main() {
    println!("{}", good_vs_evil("0 0 0 0 0 10", "0 0 0 0 0 0 0"));
}