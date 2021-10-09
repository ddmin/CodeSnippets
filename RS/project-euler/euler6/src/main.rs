fn sum_of_squares(n: i64) -> i64 {
    let mut sum: i64 = 0;
    (1..=n).for_each(|x| sum += x*x);
    sum
}

fn square_of_sums(n: i64) -> i64 {
    let mut sum: i64 = 0;
    (1..=n).for_each(|x| sum += x);
    sum * sum
}

fn main() {
    let n = 100;
    let sum = sum_of_squares(n);
    let square = square_of_sums(n);
    println!("Difference: {}", square-sum);
}
