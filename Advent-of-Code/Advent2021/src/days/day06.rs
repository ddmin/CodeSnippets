use crate::*;

const INPUT: &str = include_str!("../../inputs/day06.txt");

fn collate(lanternfish: Vec<i32>) -> Vec<i64> {
    let mut collated = (0..=8).map(|_| 0).collect::<Vec<_>>();
    for fish in lanternfish {
        collated[fish as usize] += 1
    }
    collated
}

pub fn part1(input: &str, days: i32) -> i32 {
    let mut lanternfish = split(input, ",");

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
    let mut lanternfish = collate(split(input, ","));

    //  0  1  2  3  4  5  6  7  8
    //  -------------------------
    // *3  0  0  0  0  0  1  0  2   Initial State (Birthing Fish: Index 0)
    //  0  0  0  0  0  1  0  2 *3   Rotate Left   (Birthing Fish: Index 8)
    //  0  0  0  0  0  1 *3  2  3   New Fish      (New Fish:      Index 6)

    for _ in 0..days {
        lanternfish.rotate_left(1);
        lanternfish[6] += lanternfish[8];
    }
    lanternfish.iter().sum::<i64>()
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
