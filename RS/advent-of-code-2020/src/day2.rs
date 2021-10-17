pub fn part1(input: &str) {
    let lines = input.split("\n");
    for line in lines.filter(|&x| x != "") {
        let mut tokens = line.split_whitespace();

        let (lower, upper) = tokens.next().unwrap().split_once("-").unwrap();
        let letter = tokens.next().unwrap().chars().next().unwrap();
        let password = tokens.next().unwrap();

        let count = password.chars().filter(|&x| x == letter).count();
        println!("{}-{} | {} | {}", lower, upper, letter, password);
        println!("{}", count);
    }
}
