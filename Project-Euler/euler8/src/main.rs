use std::fs;

fn string_product(string: &str) -> u64 {
    let mut product: u64 = 1;
    string
        .chars()
        .for_each(
            |x| product *= x.to_digit(10).expect("Could not parse") as u64
        );
    product
}

fn main() {
    const DIGITS: usize = 13;
    let contents = fs::read_to_string("input.txt")
        .expect("Could not read file");
    let mut largest = 0;

    for i in 0..contents.len()-DIGITS {
        let product = string_product(&contents[i..i+DIGITS]);
        if product > largest {
            largest = product;
        }
    }
    println!("{}", largest);
}
