use crate::*;

const INPUT: &str = include_str!("../../inputs/day07.txt");

fn calculate_fuel(position: i32, destination: i32) -> i32 {
    (position - destination).abs()
}

fn calculate_crab_fuel(position: i32, destination: i32) -> i32 {
    gauss((position - destination).abs())
}

// Sum all numbers 1 to n.
//      1   2   3   4   5  ...   46  47  48  49  50
//  + 100  99  98  97  96  ...   55  54  53  52  51
//  -----------------------------------------------
//    101 101 101 101 101  ...  101 101 101 101 101
// 101 * 50 = 5050
fn gauss(n: i32) -> i32 {
    n * (n + 1) / 2
}

pub fn part1(input: &str) -> i32 {
    let mut positions = split(input, ",");
    positions.sort_unstable();

    let (min, max) = (positions[0], positions[positions.len() - 1]);

    (min..=max)
        .map(|dest| {
            positions
                .iter()
                .map(move |&pos| calculate_fuel(dest, pos))
                .sum::<i32>()
        })
        .min()
        .unwrap()
}

pub fn part2(input: &str) -> i32 {
    let mut positions = split(input, ",");
    positions.sort_unstable();

    let (min, max) = (positions[0], positions[positions.len() - 1]);

    (min..=max)
        .map(|dest| {
            positions
                .iter()
                .map(move |&pos| calculate_crab_fuel(pos, dest))
                .sum::<i32>()
        })
        .min()
        .unwrap()
}

pub fn run() {
    println!("Part 1: {}", part1(INPUT));
    println!("Part 2: {}", part2(INPUT));
}

#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE: &str = include_str!("../../examples/day07.txt");

    #[test]
    fn example1() {
        assert_eq!(part1(EXAMPLE), 37);
    }

    #[test]
    fn example2() {
        assert_eq!(part2(EXAMPLE), 168);
    }
}
