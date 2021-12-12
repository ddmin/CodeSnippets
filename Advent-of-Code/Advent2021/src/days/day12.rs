use crate::*;
use std::collections::HashMap;
use std::str::FromStr;

const INPUT: &str = include_str!("../../inputs/day12.txt");

fn is_lowercase(s: &str) -> bool {
    s.chars().map(|c| ('a'..='z').contains(&c)).all(|bool| bool)
}

enum Cave {
    Start,
    Big(String),
    Small(String),
    End,
}

impl fmt::Debug for Cave {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            Cave::Start => write!(f, "start"),
            Cave::End => write!(f, "end"),
            Cave::Small(s) => write!(f, "{}", s),
            Cave::Big(s) => write!(f, "{}", s),
        }
    }
}

impl FromStr for Cave {
    type Err = ();
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "start" => Ok(Cave::Start),
            "end" => Ok(Cave::End),
            s if is_lowercase(s) => Ok(Cave::Small(s.to_string())),
            s if !is_lowercase(s) => Ok(Cave::Big(s.to_string())),
            _ => unreachable!(),
        }
    }
}

fn parse_input(input: &str) -> Vec<(Cave, Cave)> {
    let input = bifurcate(input, "-");
    input
        .iter()
        .map(|(a, b)| (Cave::from_str(*a).unwrap(), Cave::from_str(*b).unwrap()))
        .collect()
}

pub fn part1(input: &str) -> i32 {
    let connections = parse_input(input);
    println!("{:?}", connections);
    0
}

#[allow(unused)]
pub fn part2(input: &str) -> i32 {
    0
}

pub fn run() {
    println!("Part 1: {}", part1(INPUT));
    println!("Part 2: {}", part2(INPUT));
}

#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE_1: &str = include_str!("../../examples/day12-1.txt");
    const EXAMPLE_2: &str = include_str!("../../examples/day12-2.txt");
    const EXAMPLE_3: &str = include_str!("../../examples/day12-3.txt");

    #[test]
    fn example1_1() {
        assert_eq!(part1(EXAMPLE_1), 10);
    }

    #[test]
    fn example1_2() {
        assert_eq!(part1(EXAMPLE_2), 19);
    }

    #[test]
    fn example1_3() {
        assert_eq!(part1(EXAMPLE_3), 226);
    }

    #[test]
    fn example2() {
        assert_eq!(part2(EXAMPLE_1), 0);
    }
}
