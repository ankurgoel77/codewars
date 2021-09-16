// https://www.codewars.com/kata/5e2596a9ad937f002e510435/train/rust

fn infected(s: &str) -> f64 {
    let mut total:usize = 0;
    let mut infected:usize = 0;
    let countries = s.split("X");
    for country in countries {
        total += country.len();
        if country.contains("1") {
            infected += country.len();
        }
    }
    match total {
        0 => 0.0,
        _ => 100.0 * (infected as f64) / (total as f64),
    }
}