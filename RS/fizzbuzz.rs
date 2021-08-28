fn fizz_buzz(n: u32, divisors: [(u32, &str); 3]) -> String {
    let mut base = String::from("");

    for i in 0..3 {
        if n % divisors[i].0 == 0 {
            base = base + divisors[i].1;
        }
    }
    return base;
}

fn main() {
    let d: [(u32, &str); 3] = [(3, "Fizz"), (5, "Buzz"), (7, "Baxx")];

    for i in 1..1001 {
        println!("{:04}   {}", i, fizz_buzz(i, d));
    }
}
