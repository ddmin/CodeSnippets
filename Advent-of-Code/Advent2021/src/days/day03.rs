#![allow(unused_imports)]
use crate::*;

const INPUT: &str = include_str!("../../inputs/day03.txt");

// 1 4 7        1 2 3
// 2 5 8   =>   4 5 6
// 3 6 9        7 8 9
fn transpose(input: &str) -> Vec<Vec<&u8>> {
    let mut vec = Vec::new();
    for line in input.lines() {
        for (idx, byte) in line.as_bytes().iter().enumerate() {
            if idx >= vec.len() {
                vec.push(Vec::new());
            }
            vec[idx].push(byte);
        }
    }
    vec
}

pub fn part1(input: &str) -> i32 {
    let vec = transpose(input);
    let tuples = vec
        .iter()
        .map(|vec| {
            vec.iter().fold((0, 0), |(x, y), byte| match byte {
                b'0' => (x + 1, y),
                b'1' => (x, y + 1),
                _ => unreachable!(),
            })
        })
        .collect::<Vec<_>>();

    let gamma = tuples
        .iter()
        .map(|(x, y)| if x > y { '0' } else { '1' })
        .collect::<String>();

    let bitmask = vec!['1'; gamma.len()].iter().collect::<String>();
    let bitmask = i32::from_str_radix(&bitmask, 2).unwrap();

    let gamma = i32::from_str_radix(&gamma, 2).unwrap();
    let epsilon = gamma ^ bitmask;

    gamma * epsilon
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
    const EXAMPLE: &str = include_str!("../../examples/day03.txt");

    #[test]
    fn example1() {
        assert_eq!(part1(EXAMPLE), 198);
    }

    #[test]
    fn example2() {
        assert_eq!(part2(EXAMPLE), 0);
    }
}
