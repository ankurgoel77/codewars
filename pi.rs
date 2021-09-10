fn rnd10(f: f64) -> f64 { (f * 1e10).round() / 1e10 }

fn iter_pi(epsilon: f64) -> (i32, f64) {
    let mut count:i32 = 0;
    let mut pi:f64 = 0.0;
    while f64::abs(pi*4.0 - std::f64::consts::PI) > epsilon {
        pi += ((-1i32).pow(count as u32) as f64) / ((count*2 + 1) as f64);
        count += 1;
        println!("{} : {}", count, pi*4.0);
    }
    return (count, rnd10(pi));
}

fn main() {
    println!("{}", std::f64::consts::PI);
    iter_pi(0.01);
}

