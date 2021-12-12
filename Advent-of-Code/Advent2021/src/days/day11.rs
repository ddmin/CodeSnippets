use crate::*;
use std::collections::HashSet;

const INPUT: &str = include_str!("../../inputs/day11.txt");

type Coordinate = (usize, usize);

struct Grid {
    grid: Vec<Vec<i32>>,
    height: usize,
    width: usize,
    flashes: i32,
}

impl Grid {
    fn new(input: &str) -> Grid {
        let grid = input
            .lines()
            .map(|line| {
                line.chars()
                    .map(|c| c as u8 - '0' as u8)
                    .map(|n| n as i32)
                    .collect::<Vec<_>>()
            })
            .collect::<Vec<_>>();

        let (height, width) = (grid.len() - 1, grid[0].len() - 1);

        Grid {
            grid,
            height,
            width,
            flashes: 0,
        }
    }

    fn get(&self, coordinate: Coordinate) -> i32 {
        let (x, y) = coordinate;
        self.grid[y][x]
    }

    fn get_mut(&mut self, coordinate: Coordinate) -> &mut i32 {
        let (x, y) = coordinate;
        self.grid.get_mut(y).unwrap().get_mut(x).unwrap()
    }

    fn flashes(&self) -> i32 {
        self.flashes
    }

    fn all_flashed(&self) -> bool {
        for y in 0..=self.height {
            for x in 0..=self.width {
                if self.get((x, y)) != 0 {
                    return false;
                }
            }
        }
        true
    }

    fn adjacent(&self, coordinate: Coordinate) -> Vec<Coordinate> {
        let (x, y) = (coordinate.0 as i32, coordinate.1 as i32);
        let (x_lower, x_upper, y_lower, y_upper) =
            (x > 0, x < self.width as i32, y > 0, y < self.height as i32);
        [
            (x_lower && y_lower, (x - 1, y - 1)),
            (y_lower, (x, y - 1)),
            (x_upper && y_lower, (x + 1, y - 1)),
            (x_lower, (x - 1, y)),
            (x_upper, (x + 1, y)),
            (x_lower && y_upper, (x - 1, y + 1)),
            (y_upper, (x, y + 1)),
            (x_upper && y_upper, (x + 1, y + 1)),
        ]
        .into_iter()
        .filter(|(condition, _)| *condition)
        .map(|(_, (x, y))| (x as usize, y as usize))
        .collect()
    }

    fn step(&mut self, n: usize) {
        for _ in 0..n {
            let mut to_flash = Vec::new();
            let mut flashed = HashSet::new();
            for y in 0..=self.height {
                for x in 0..=self.width {
                    *self.get_mut((x, y)) += 1;
                    if self.get((x, y)) > 9 {
                        to_flash.push((x, y));
                    }
                }
            }

            while let Some(coordinate) = to_flash.pop() {
                if !flashed.insert(coordinate) {
                    continue;
                }

                self.adjacent(coordinate)
                    .into_iter()
                    .for_each(|coordinate| {
                        *self.get_mut(coordinate) += 1;
                        if self.get(coordinate) > 9 {
                            to_flash.push(coordinate);
                        }
                    });
            }

            flashed.iter().for_each(|&coordinate| {
                self.flashes += 1;
                *self.get_mut(coordinate) = 0;
            });
        }
    }
}

impl fmt::Debug for Grid {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        for rows in self.grid.iter() {
            writeln!(
                f,
                "{}",
                rows.iter().map(|n| n.to_string()).collect::<String>()
            )?;
        }
        write!(f, "")
    }
}

pub fn part1(input: &str) -> i32 {
    let mut octopi = Grid::new(input);
    octopi.step(100);
    octopi.flashes()
}

pub fn part2(input: &str) -> i32 {
    let mut octopi = Grid::new(input);

    let mut count = 0;
    while !octopi.all_flashed() {
        octopi.step(1);
        count += 1;
    }
    count
}

pub fn run() {
    println!("Part 1: {}", part1(INPUT));
    println!("Part 2: {}", part2(INPUT));
}

#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE: &str = include_str!("../../examples/day11.txt");

    #[test]
    fn example1() {
        assert_eq!(part1(EXAMPLE), 1656);
    }

    #[test]
    fn example2() {
        assert_eq!(part2(EXAMPLE), 195);
    }
}
