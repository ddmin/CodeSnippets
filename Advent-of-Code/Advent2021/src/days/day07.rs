use crate::*;

const INPUT: &str = include_str!("../../inputs/day07.txt");

fn calculate_fuel(position: i32, destination: i32) -> i32 {
    (position - destination).abs()
}

fn calculate_crab_fuel(position: i32, destination: i32) -> i32 {
    (1..=(position - destination).abs()).sum()
}

pub fn part1(input: &str) -> i32 {
    let mut positions = split(input, ",");
    positions.sort_unstable();

    let mut fuels_fuels = Vec::new();
    for destination in positions[0]..=positions[positions.len() - 1] {
        let mut fuels = Vec::new();
        for &position in positions.iter() {
            let fuel = calculate_fuel(position, destination);
            fuels.push(fuel);
        }
        fuels_fuels.push(fuels.iter().sum::<i32>());
    }
    *fuels_fuels.iter().min().unwrap()
}

pub fn part2(input: &str) -> i32 {
    let mut positions = split(input, ",");
    positions.sort_unstable();

    let mut fuels_fuels = Vec::new();
    for destination in positions[0]..=positions[positions.len() - 1] {
        let mut fuels = Vec::new();
        for &position in positions.iter() {
            let fuel = calculate_crab_fuel(position, destination);
            fuels.push(fuel);
        }
        fuels_fuels.push(fuels.iter().sum::<i32>());
    }
    *fuels_fuels.iter().min().unwrap()
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
        assert_eq!(part1(EXAMPLE), 0);
    }

    #[test]
    fn example2() {
        assert_eq!(part2(EXAMPLE), 0);
    }
}
