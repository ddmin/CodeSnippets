pub fn part1(input: &str) {
    let mut lookup: Vec<i32> = Vec::new();
    for num in input.split_whitespace() {
        let n: i32 = num.parse().unwrap();
        if lookup.contains(&(2020 - n)) {
            println!("Part 1: {} x {} = {}", n, 2020 - n, n * (2020 - n));
            ()
        }
        lookup.push(n);
    }
}

pub fn part2(input: &str) {

    let lines: Vec<i32> = input
        .split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();

    for a in 0..=lines.len() - 3 {
        let first = lines.get(a).unwrap();
        for b in a..=lines.len() - 2 {
            let second = lines.get(b).unwrap();
            let to_find = 2020 - (first + second);
            for c in b..lines.len() {
                let third = lines.get(c).unwrap();
                if *third == to_find {
                    println!(
                        "Part 2: {} x {} x {} = {}",
                        first,
                        second,
                        third,
                        first * second * third
                    );
                }
            }
        }
    }
}
