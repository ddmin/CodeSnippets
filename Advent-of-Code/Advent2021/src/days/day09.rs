const INPUT: &str = include_str!("../../inputs/day09.txt");

type HeightMap = Vec<Vec<i32>>;

fn parse_input(input: &str) -> HeightMap {
    input
        .lines()
        .map(|line| {
            line.chars()
                .map(|c| c.to_string().parse::<i32>().unwrap())
                .collect::<Vec<_>>()
        })
        .collect()
}

fn neighbors(grid: &[Vec<i32>], x: usize, y: usize) -> Vec<i32> {
    let width: usize = grid[0].len() - 1;
    let height: usize = grid.len() - 1;

    let mut neighbors = Vec::new();

    // Adjacent Left Neighbor
    if x != 0 {
        neighbors.push(grid[y][x - 1]);
    }

    // Adjacent Right Neighbor
    if x < width {
        neighbors.push(grid[y][x + 1]);
    }

    // Adjacent Bottom Neighbor
    if y < height {
        neighbors.push(grid[y + 1][x]);
    }

    // Adjacent Top Neighbor
    if y != 0 {
        neighbors.push(grid[y - 1][x]);
    }
    neighbors
}

fn is_lowest(n: i32, neighbors: &[i32]) -> bool {
    neighbors.iter().find(|&&x| n >= x).is_none()
}

pub fn part1(input: &str) -> i32 {
    let heightmap = parse_input(input);

    (0..heightmap.len())
        .map(|y| {
            (0..heightmap[y].len())
                .filter(|&x| is_lowest(heightmap[y][x], &neighbors(&heightmap, x, y)))
                .fold(0, |acc, x| acc + 1 + heightmap[y][x])
        })
        .sum()
}

pub fn part2(input: &str) -> i32 {
    let _heightmap = parse_input(input);
    0
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
