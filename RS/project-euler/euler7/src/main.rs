fn is_prime(n: i64) -> bool {
    let upper_limit = (n as f64).sqrt() as i64 + 1;

    for i in 2..=upper_limit {
        if n % i == 0 {
            return false
        }
    }
    true
}

fn main() {
    const TARGET: i32 = 10_000;
    let mut found_primes = 0;
    let mut num = 1;
    while found_primes != TARGET {
        num += 1;
        if is_prime(num) {
            found_primes += 1;
        }
    }
    println!("Prime: {}", num);
}
