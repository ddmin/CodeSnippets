struct Fibonacci {
    curr: i32,
    next: i32,
}

impl Fibonacci {
    fn new() -> Fibonacci {
        Fibonacci { curr: 1, next: 1 }
    }
}

impl Iterator for Fibonacci {
    type Item = i32;

    fn next(&mut self) -> Option<Self::Item> {
        let new_next = self.curr + self.next;

        self.curr = self.next;
        self.next = new_next;

        Some(self.curr)
    }
}

fn main() {
    let mut sum = 0;
    let fibonacci = Fibonacci::new();
    const UPPER_LIMIT: i32 = 4_000_000;

    for n in fibonacci {
        match n {
            n if n > UPPER_LIMIT => break,
            n if n % 2 == 0 => sum += n,
            _ => continue,
        }
    }
    println!("Sum: {}", sum);
}
