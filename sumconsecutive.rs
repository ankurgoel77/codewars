// https://www.codewars.com/kata/55eeddff3f64c954c2000059/train/rust

/// Just to make code nicer
type Number = i32;
type Numbers = Vec<Number>;

/// Sums the numbers that are the same and consecutive.
fn sum_consecutives(numbers: &Numbers) -> Numbers {
    let mut sum = numbers[0];
    let mut previous = numbers[0];
    let mut result: Numbers = Vec::new();

    for i in 1..numbers.len() {
        if numbers[i] == previous {
            sum += numbers[i]
        } else {
            result.push(sum);
            previous = numbers[i];
            sum = previous;
        }
    }
    result.push(sum);
    result
}