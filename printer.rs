fn printer_error(s: &str) -> String {
    let mut count : i32 = 0;
    for c in s.chars() {
        if c > 'm' {
            count +=1;
        }
    }
    return format!("{}/{}", count, s.len())
}

fn main() {
    println!("{}",printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"));
}