use crate::*;
use std::collections::HashMap;

struct Grid {
    hashmap: HashMap<(i32, i32), i32>,
    width: i32,
    height: i32,
}

impl Grid {
    fn new() -> Grid {
        Grid {
            hashmap: HashMap::new(),
            width: 0,
            height: 0,
        }
    }

    fn insert(&mut self, item: (i32, i32)) {
        let entry = self.hashmap.entry(item).or_insert(0);
        *entry += 1;
    }

    fn extend_width(&mut self, widths: (i32, i32)) {
        self.width = if self.width < widths.0 {
            widths.0
        } else if self.width < widths.1 {
            widths.1
        } else {
            self.width
        }
    }

    fn extend_height(&mut self, heights: (i32, i32)) {
        self.height = if self.height < heights.0 {
            heights.0
        } else if self.height < heights.1 {
            heights.1
        } else {
            self.height
        }
    }
}

impl fmt::Display for Grid {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        for w in 0..=self.width {
            for h in 0..=self.height {
                write!(f, "{}", self.hashmap.get(&(h, w)).unwrap_or(&0))?;
            }
            writeln!(f)?;
        }
        write!(f, "")
    }
}

const INPUT: &str = include_str!("../../inputs/day05.txt");

type Pairs = Vec<Vec<(i32, i32)>>;

fn parse_input(input: &str) -> Pairs {
    let input = bifurcate(input, " -> ");
    let input = input.iter().map(|(a, b)| vec![a, b]).collect::<Vec<_>>();

    input
        .iter()
        .map(|pair| {
            pair.iter()
                .map(|pair| pair.split_once(",").unwrap())
                .map(|(a, b)| (a.parse::<i32>().unwrap(), b.parse::<i32>().unwrap()))
                .collect::<Vec<_>>()
        })
        .collect()
}

pub fn part1(input: &str) -> i32 {
    let input = parse_input(input);

    let mut grid = Grid::new();
    for range in input {
        let (x1, y1) = range[0];
        let (x2, y2) = range[1];

        if x1 == x2 {
            let range = if y2 > y1 {
                0..=(y2 - y1)
            } else {
                (y2 - y1)..=0
            };
            for y in range {
                grid.insert((x1, y1 + y))
            }
        } else if y1 == y2 {
            let range = if x2 > x1 {
                0..=(x2 - x1)
            } else {
                (x2 - x1)..=0
            };
            for x in range {
                grid.insert((x1 + x, y1))
            }
        }
        grid.extend_width((x1, x2));
        grid.extend_height((y1, y2));
    }
    grid.hashmap.values().filter(|&&x| x > 1).count() as i32
}

pub fn part2(input: &str) -> i32 {
    let input = parse_input(input);

    let mut grid = Grid::new();
    for range in input {
        let (x1, y1) = range[0];
        let (x2, y2) = range[1];

        if x1 == x2 {
            let range = if y2 > y1 {
                0..=(y2 - y1)
            } else {
                (y2 - y1)..=0
            };
            range.for_each(|y| grid.insert((x1, y1 + y)));
        } else if y1 == y2 {
            let range = if x2 > x1 {
                0..=(x2 - x1)
            } else {
                (x2 - x1)..=0
            };
            range.for_each(|x| grid.insert((x1 + x, y1)));
        } else {
            let range_x: Vec<_> = if x2 > x1 {
                (0..=(x2 - x1)).collect()
            } else {
                ((x2 - x1)..=0).rev().collect()
            };

            let range_y: Vec<_> = if y2 > y1 {
                (0..=(y2 - y1)).collect()
            } else {
                ((y2 - y1)..=0).rev().collect()
            };

            range_x
                .iter()
                .zip(range_y.iter())
                .for_each(|(x, y)| grid.insert((x1 + x, y1 + y)));
        }
        grid.extend_width((x1, x2));
        grid.extend_height((y1, y2));
    }
    grid.hashmap.values().filter(|&&x| x > 1).count() as i32
}

pub fn run() {
    println!("Part 1: {}", part1(INPUT));
    println!("Part 2: {}", part2(INPUT));
}

#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE: &str = include_str!("../../examples/day05.txt");

    #[test]
    fn example1() {
        assert_eq!(part1(EXAMPLE), 5);
    }

    #[test]
    fn example2() {
        assert_eq!(part2(EXAMPLE), 12);
    }
}
