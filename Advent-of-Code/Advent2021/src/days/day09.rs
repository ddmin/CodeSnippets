use std::collections::HashSet;

const INPUT: &str = include_str!("../../inputs/day09.txt");

type Coordinate = (i32, i32);

struct Heightmap {
    map: Vec<Vec<i32>>,
}

impl Heightmap {
    fn new(input: &str) -> Heightmap {
        Heightmap {
            map: input
                .lines()
                .map(|line| {
                    line.chars()
                        .map(|c| c.to_string().parse::<i32>().unwrap())
                        .collect::<Vec<_>>()
                })
                .collect(),
        }
    }

    fn height(&self) -> i32 {
        self.map.len() as i32
    }

    fn width(&self) -> i32 {
        self.map[0].len() as i32
    }

    fn get(&self, coordinate: Coordinate) -> i32 {
        let (x, y) = coordinate;
        self.map[y as usize][x as usize]
    }

    fn neighbors(&self, coordinate: Coordinate) -> Vec<Coordinate> {
        let (x, y) = coordinate;

        let width = (self.map[0].len() - 1) as i32;
        let height = (self.map.len() - 1) as i32;

        [
            (x != 0, (x - 1, y)),
            (x < width, (x + 1, y)),
            (y != 0, (x, y - 1)),
            (y < height, (x, y + 1)),
        ]
        .into_iter()
        .filter(|(condition, _)| *condition)
        .map(|(_, coordinate)| coordinate)
        .collect()
    }

    fn is_low_point(&self, coordinate: Coordinate) -> bool {
        !self
            .neighbors(coordinate)
            .iter()
            .any(|&neighbor| self.get(coordinate) >= self.get(neighbor))
    }
}

pub fn part1(input: &str) -> i32 {
    let heightmap = Heightmap::new(input);

    (0..heightmap.height())
        .map(|y| {
            (0..heightmap.width())
                .filter(|&x| heightmap.is_low_point((x, y)))
                .fold(0, |acc, x| acc + 1 + heightmap.get((x, y)))
        })
        .sum()
}

pub fn part2(input: &str) -> i32 {
    let heightmap = Heightmap::new(input);

    let low_points = (0..heightmap.height())
        .map(|y| {
            (0..heightmap.width())
                .filter(|&x| heightmap.is_low_point((x, y)))
                .map(|x| (x, y))
                .collect::<Vec<_>>()
        })
        .flatten();

    let mut basins = low_points
        .map(|low_point| {
            let mut to_visit = vec![low_point];
            let mut visited = HashSet::new();
            while let Some(coordinate) = to_visit.pop() {
                if !visited.insert(coordinate) {
                    continue;
                }
                heightmap
                    .neighbors(coordinate)
                    .into_iter()
                    .filter(|&neighbor| {
                        heightmap.get(neighbor) != 9
                            && heightmap.get(neighbor) > heightmap.get(coordinate)
                    })
                    .for_each(|neighbor| {
                        to_visit.push(neighbor);
                    })
            }
            visited.len()
        })
        .collect::<Vec<_>>();

    basins.sort();

    basins.iter().rev().take(3).product::<usize>() as i32
}

pub fn run() {
    println!("Part 1: {}", part1(INPUT));
    println!("Part 2: {}", part2(INPUT));
}

#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE: &str = include_str!("../../examples/day09.txt");

    #[test]
    fn example1() {
        assert_eq!(part1(EXAMPLE), 15);
    }

    #[test]
    fn example2() {
        assert_eq!(part2(EXAMPLE), 1134);
    }
}
