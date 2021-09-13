// https://www.codewars.com/kata/513e08acc600c94f01000001/train/rust

// fn clamp(i:i32) -> u8 {
//     if i > 255 {
//         return 255u8;
//     } else if i < 0 {
//         return 0u8;
//     }
//     i as u8
// }

// fn rgb(r: i32, g: i32, b: i32) -> String {
//     String::from(format!("{:02X}{:02X}{:02X}",clamp(r),clamp(g),clamp(b)))
// }

fn rgb(r: i32, g: i32, b: i32) -> String {
    String::from(format!("{:02X}{:02X}{:02X}",r.clamp(0,255), g.clamp(0,255), b.clamp(0,255)))
  }
