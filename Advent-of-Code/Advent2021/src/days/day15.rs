use std::cmp::Ordering;
use std::collections::{BinaryHeap, HashMap};

const INPUT: &str = include_str!("../../inputs/day15.txt");

type Cave = Vec<Vec<usize>>;
type Coordinate = (usize, usize);

#[derive(Debug, Copy, Clone, Eq, PartialEq)]
struct RiskLevel {
    risk: usize,
    position: Coordinate,
}

impl Ord for RiskLevel {
    fn cmp(&self, other: &Self) -> Ordering {
        other
            .risk
            .cmp(&self.risk)
            .then_with(|| manhattan(self.position, (0, 0)).cmp(&manhattan(other.position, (0, 0))))
    }
}

impl PartialOrd for RiskLevel {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

fn manhattan((x1, y1): Coordinate, (x2, y2): Coordinate) -> usize {
    ((x2 as i32 - x1 as i32).abs() + (y2 as i32 - y1 as i32).abs())
        .try_into()
        .unwrap()
}

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

fn full_map(cave: &[Vec<usize>]) -> Cave {
    let mut entire_cave = Vec::new();
    for y in 0..cave.len() * 5 {
        entire_cave.push(Vec::new());
        for x in 0..cave[0].len() * 5 {
            entire_cave[y].push({
                let risk = cave[y % cave.len()][x % cave[0].len()]
                    + (y / cave.len())
                    + (x / cave[0].len());
                if risk < 10 {
                    risk
                } else {
                    risk - 9
                }
            });
        }
    }
    entire_cave
}

fn find_neighbors((x, y): Coordinate, cave: &[Vec<usize>]) -> Vec<Coordinate> {
    [
        (x < cave[0].len() - 1, (x as i32 + 1, y as i32)),
        (y < cave.len() - 1, (x as i32, y as i32 + 1)),
        (x != 0, (x as i32 - 1, y as i32)),
        (y != 0, (x as i32, y as i32 - 1)),
    ]
    .into_iter()
    .filter(|(condition, _)| *condition)
    .map(|(_, (x, y))| (x as usize, y as usize))
    .collect::<Vec<_>>()
}

// use Dijkstra's Algorithm to find the path with the lowest risk level.
fn find_lowest_risk(
    cave: &[Vec<usize>],
    neighbors: &HashMap<Coordinate, Vec<Coordinate>>,
) -> usize {
    // coordinates to visit next
    let mut to_visit = BinaryHeap::new();

    // hashmap of the accrued risk levels to a coordinate
    let mut risk_levels = HashMap::new();

    for (y, row) in cave.iter().enumerate() {
        for x in 0..row.len() {
            risk_levels.insert((x, y), usize::MAX);
        }
    }

    // start at (0, 0)
    *risk_levels.get_mut(&(0, 0)).unwrap() = 0;
    to_visit.push(RiskLevel {
        risk: 0,
        position: (0, 0),
    });

    while let Some(RiskLevel { risk, position }) = to_visit.pop() {
        // the end of the cave has been reached, return the risk level
        if position == (cave[0].len() - 1, cave.len() - 1) {
            return risk;
        }

        // if a lower-risk path already exists, continue searching
        if risk > risk_levels[&position] {
            continue;
        }

        // search the adjacent chiton densities
        for (x, y) in &neighbors[&position] {
            let next = RiskLevel {
                risk: risk + cave[*y][*x],
                position: (*x, *y),
            };

            // if a lower-risk path exists, use the lower-risk path
            if next.risk < risk_levels[&next.position] {
                to_visit.push(next);
                *risk_levels.get_mut(&next.position).unwrap() = next.risk;
            }
        }
    }

    unreachable!()
}

pub fn part1(input: &str) -> i32 {
    let cave = parse_input(input);
    let mut neighbors = HashMap::new();

    for y in 0..cave.len() {
        for x in 0..cave[y].len() {
            neighbors.insert((x, y), find_neighbors((x, y), &cave));
        }
    }

    find_lowest_risk(&cave, &neighbors) as i32
}

pub fn part2(input: &str) -> i32 {
    let cave = full_map(&parse_input(input));
    let mut neighbors = HashMap::new();

    for y in 0..cave.len() {
        for x in 0..cave[y].len() {
            neighbors.insert((x, y), find_neighbors((x, y), &cave));
        }
    }

    find_lowest_risk(&cave, &neighbors) as i32
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
        assert_eq!(part2(EXAMPLE), 315);
    }
}
