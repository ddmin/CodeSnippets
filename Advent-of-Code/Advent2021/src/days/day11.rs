const INPUT: &str = include_str!("../../inputs/day11.txt");

type Coordinate = (i32, i32);

struct Grid {
    grid: Vec<Vec<i32>>,
    height: i32,
    width: i32,
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

        let (height, width) = (grid.len() as i32 - 1, grid[0].len() as i32 - 1);

        Grid {
            grid,
            height,
            width,
            flashes: 0,
        }
    }

    fn adjacent(&self, coordinate: Coordinate) -> Vec<Coordinate> {
        let (x, y) = coordinate;
        let (x_lower, x_upper, y_lower, y_upper) = (x > 0, x < self.width, y > 0, y < self.height);
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
        .map(|(_, coordinate)| coordinate)
        .collect()
    }

    fn step(&mut self) {}
}

pub fn part1(input: &str) -> i32 {
    let mut octopi = Grid::new(input);
    println!("{:?}", octopi.grid);
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
    const EXAMPLE: &str = include_str!("../../examples/day11.txt");

    #[test]
    fn example1() {
        assert_eq!(part1(EXAMPLE), 1656);
    }

    #[test]
    fn example2() {
        assert_eq!(part2(EXAMPLE), 0);
    }
}
