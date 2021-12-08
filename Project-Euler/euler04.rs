fn is_pallindrome(num: i32) -> bool {
    let num: String = num.to_string();
    let reversed: String = num.chars().rev().collect();

    num == reversed
}

fn main() {
    let mut largest = 0;

    for x in 100..=999 {
        for y in 100..=999 {
            if is_pallindrome(x*y) && x*y > largest {
                largest = x*y;
            }
        }
    }

    println!("Largest: {}", largest);
}
