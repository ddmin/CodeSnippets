fn is_prime(n: i64) -> bool {
    let upper_limit = (n as f64).sqrt() as i64 + 1;

    for i in 2..upper_limit {
        if n % i == 0 {
            return false
        }
    }
    true
}

fn main() {
    const UPPER: i64 = 2_000_000;
    let mut primes: Vec<i64> = Vec::new();
    for n in 2..=UPPER {
        if is_prime(n) {
            primes.push(n);
        }
    }

    let sum: i64 = primes.iter().sum();
    println!("Sum: {}", sum);
}
