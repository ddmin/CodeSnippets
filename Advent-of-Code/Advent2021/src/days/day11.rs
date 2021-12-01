#![allow(unused_imports)]
use crate::*;

const INPUT: &str = include_str!("../../inputs/day11.txt");

#[allow(unused)]
pub fn part1(input: &str) -> i32 {
    0
}

#[allow(unused)]
pub fn part2(input: &str) -> i32 {
    0
}

pub fn run() {
    println!("{}", part1(INPUT));
    println!("{}", part2(INPUT));
}

#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE: &str = include_str!("../../examples/day11.txt");

    #[test]
    fn example1() {
        assert_eq!(part1(EXAMPLE), 0);
    }

    #[test]
    fn example2() {
        assert_eq!(part2(EXAMPLE), 0);
    }
}
