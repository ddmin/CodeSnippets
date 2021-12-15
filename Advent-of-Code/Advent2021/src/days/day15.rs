const INPUT: &str = include_str!("../../inputs/day15.txt");

type Cave = Vec<Vec<usize>>;
type Coordinate = (usize, usize);

fn parse_input(input: &str) -> Cave {
    input
        .lines()
        .map(|line| {
            line.chars()
                .map(|c| c.to_digit(10).unwrap() as usize)
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>()
}

fn find_neighbors((x, y): Coordinate, cave: &Cave) -> Vec<Coordinate> {
    [
        (x < cave[0].len() - 1, (x + 1, y)),
        (y < cave.len() - 1, (x, y + 1)),
    ]
    .into_iter()
    .filter(|(condition, _)| *condition)
    .map(|(_, coordinate)| coordinate)
    .collect::<Vec<_>>()
}

fn find_lowest_risk((x, y): Coordinate, risk_level: usize, cave: &Cave) -> usize {
    if (x, y) == (cave[0].len() - 1, cave.len() - 1) {
        return risk_level;
    }

    let mut risk_levels = find_neighbors((x, y), &cave)
        .into_iter()
        .map(|(nx, ny)| find_lowest_risk((nx, ny), risk_level + cave[ny][nx], &cave))
        .collect::<Vec<_>>();

    risk_levels.sort();

    *risk_levels.get(0).unwrap()
}

pub fn part1(input: &str) -> i32 {
    let cave = parse_input(input);
    find_lowest_risk((0, 0), 0, &cave) as i32
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
    const EXAMPLE: &str = include_str!("../../examples/day15.txt");

    #[test]
    fn example1() {
        assert_eq!(part1(EXAMPLE), 40);
    }

    #[test]
    fn example2() {
        assert_eq!(part2(EXAMPLE), 0);
    }
}
