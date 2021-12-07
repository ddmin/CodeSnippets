const INPUT: &str = include_str!("../../inputs/day06.txt");

pub fn part1(input: &str, days: i32) -> i32 {
    let mut lanternfish = input
        .split(',')
        .map(|n| n.parse::<i32>().unwrap())
        .collect::<Vec<_>>();

    for _ in 0..days {
        let mut new_fish = Vec::new();
        lanternfish = lanternfish
            .iter()
            .map(|&n| {
                if n == 0 {
                    new_fish.push(8);
                    6
                } else {
                    n - 1
                }
            })
            .collect();
        lanternfish.append(&mut new_fish);
    }
    lanternfish.len() as i32
}

pub fn part2(input: &str, days: i32) -> i64 {
    let mut lanternfish = input
        .split(',')
        .map(|n| n.parse::<i32>().unwrap())
        .collect::<Vec<_>>();

    for _ in 0..days {
        let mut new_fish = Vec::new();
        lanternfish = lanternfish
            .iter()
            .map(|&n| {
                if n == 0 {
                    new_fish.push(8);
                    6
                } else {
                    n - 1
                }
            })
            .collect();
        lanternfish.append(&mut new_fish);
    }
    lanternfish.len() as i64
}

pub fn run() {
    println!("Part 1: {}", part1(INPUT, 80));
    println!("Part 2: {}", part2(INPUT, 256));
}

#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE: &str = include_str!("../../examples/day06.txt");

    #[test]
    fn example1() {
        assert_eq!(part1(EXAMPLE, 18), 26);
    }

    #[test]
    fn example2() {
        assert_eq!(part2(EXAMPLE, 256), 26984457539);
    }
}
