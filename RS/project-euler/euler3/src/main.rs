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
    const NUMBER: i64 = 600851475143;
    let upper_limit = (NUMBER as f64).sqrt() as i64 + 1;

    let mut primes: Vec<i64> = Vec::new();

    for i in 2..upper_limit {
        if is_prime(i) {
            primes.push(i);
        }
    }

    let largest = primes.iter()
        .filter(|&x| NUMBER % x == 0)
        .last()
        .unwrap();

    println!("Largest: {}", largest);
}
