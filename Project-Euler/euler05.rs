fn divide_if_divisible(dividend: i64, divisor: i64) -> i64 {
    if dividend % divisor == 0 {
        return dividend / divisor
    }
    dividend
}

fn simplify(mut numbers: Vec<i64>) -> Vec<i64> {
    let mut used: Vec<i64> = Vec::new();

    while numbers.len() > 0 {
        let n = numbers.remove(0);
        used.push(n);

        numbers = numbers.iter().map(|&x| divide_if_divisible(x, n)).collect();
    }
    used
}

fn divisible_by_all(number: i64, upper: i64) -> bool {
    for i in 1..=upper {
        if number % i != 0 {
            return false
        }
    }
    true
}

fn main() {
    const UPPER: i64 = 20;
    let mut product: i64 = 1;

    let used_numbers = simplify((1..=UPPER).collect());

    used_numbers
        .iter()
        .for_each(|x| product *= x);

    if divisible_by_all(product, UPPER) {
        println!("Product: {}", product);
    }
}
