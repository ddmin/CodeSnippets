pub fn part1(input: &str) {
    let lines = input.split("\n");
    let mut valid = 0;
    for line in lines.filter(|&x| x != "") {
        let mut tokens = line.split_whitespace();

        let (lower, upper) = tokens.next().unwrap().split_once("-").unwrap();
        let lower = lower.parse::<usize>().unwrap();
        let upper = upper.parse::<usize>().unwrap();

        let letter = tokens.next().unwrap().chars().next().unwrap();
        let password = tokens.next().unwrap();

        let count = password.chars().filter(|&x| x == letter).count();
        if count >= lower && count <= upper {
            valid += 1;
        }
    }

    println!("Part 1: {}", valid);
}

pub fn part2(input: &str) {
    let lines = input.split("\n");
    let mut valid = 0;

    for line in lines.filter(|&x| x != "") {
        let mut tokens = line.split_whitespace();

        let (first, second) = tokens.next().unwrap().split_once("-").unwrap();
        let first = first.parse::<usize>().unwrap();
        let second = second.parse::<usize>().unwrap();

        let letter = tokens.next().unwrap().chars().next().unwrap();
        let password = tokens.next().unwrap();

        let letters: Vec<char> = password.chars().collect();

        let first = match letters.get(first - 1) {
            Some(c) => c,
            None => &' ',
        };

        let second = match letters.get(second - 1) {
            Some(c) => c,
            None => &' ',
        };

        if xor(first == &letter, second == &letter) {
            valid += 1;
        }
    }

    println!("Part 2: {}", valid);
}

fn xor(a: bool, b: bool) -> bool {
    (a || b) && !(a && b)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_xor() {
        assert_eq!(xor(true, true), false);
        assert_eq!(xor(false, false), false);
        assert_eq!(xor(true, false), true);
        assert_eq!(xor(false, true), true);
    }
}
