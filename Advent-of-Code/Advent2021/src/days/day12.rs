use crate::*;
use std::collections::{HashMap, HashSet};
use std::str::FromStr;

const INPUT: &str = include_str!("../../inputs/day12.txt");

fn is_lowercase(s: &str) -> bool {
    s.chars().map(|c| ('a'..='z').contains(&c)).all(|bool| bool)
}

#[derive(PartialEq, Eq, Hash, Clone)]
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
            s => Ok(Cave::Big(s.to_string())),
        }
    }
}

type CaveMap = HashMap<Cave, HashSet<Cave>>;

fn parse_input(input: &str) -> CaveMap {
    let input = bifurcate(input, "-");
    let connections = input.iter().collect::<HashSet<_>>();

    let mut map = HashMap::new();
    for (cave, connected) in connections {
        let entry = map
            .entry(Cave::from_str(cave).unwrap())
            .or_insert(HashSet::new());
        (*entry).insert(Cave::from_str(connected).unwrap());

        let entry = map
            .entry(Cave::from_str(connected).unwrap())
            .or_insert(HashSet::new());
        (*entry).insert(Cave::from_str(cave).unwrap());
    }
    map
}

fn total_paths(current: &Cave, path: &mut Vec<Cave>, map: &CaveMap, mut extra_time: bool) -> i32 {
    // if you reach the end, the path is valid
    if let Cave::End = current {
        return 1;
    }

    if path.contains(&current) {
        if let Cave::Start = current {
            // after leaving the starting point, you can't return to it
            return 0;
        } else if let Cave::Small(_) = current {
            // Part 1: there is no time to return to small caves
            if !extra_time {
                return 0;
            }
            // Part 2: you have time to visit a small cave once
            //         after visiting small cave once,
            //         you can no longer return to small caves.
            extra_time = false;
        }
    }

    // add current cave to path
    path.push(current.clone());

    let total = map
        .get(&current)
        .unwrap()
        .iter()
        .map(|cave| total_paths(cave, path, map, extra_time))
        .sum();

    path.pop();
    total
}

pub fn part1(input: &str) -> i32 {
    let connections = parse_input(input);
    total_paths(&Cave::Start, &mut Vec::new(), &connections, false)
}

pub fn part2(input: &str) -> i32 {
    let connections = parse_input(input);
    total_paths(&Cave::Start, &mut Vec::new(), &connections, true)
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
    fn example1() {
        assert_eq!(part1(EXAMPLE_1), 10);
        assert_eq!(part1(EXAMPLE_2), 19);
        assert_eq!(part1(EXAMPLE_3), 226);
    }

    #[test]
    fn example2() {
        assert_eq!(part2(EXAMPLE_1), 36);
        assert_eq!(part2(EXAMPLE_2), 103);
        assert_eq!(part2(EXAMPLE_3), 3509);
    }
}
