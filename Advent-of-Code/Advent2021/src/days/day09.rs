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

fn neighbors(grid: &[Vec<i32>], x: i32, y: i32) -> Vec<(i32, i32)> {
    let width = (grid[0].len() - 1) as i32;
    let height = (grid.len() - 1) as i32;

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

fn is_lowest(n: i32, neighbors: &[i32]) -> bool {
    !neighbors.iter().any(|&x| n >= x)
}

pub fn part1(input: &str) -> i32 {
    let heightmap = parse_input(input);

    (0..heightmap.len())
        .map(|y| {
            (0..heightmap[y].len())
                .filter(|&x| {
                    is_lowest(
                        heightmap[y][x],
                        &(neighbors(&heightmap, x as i32, y as i32)
                            .iter()
                            .map(|(x, y)| heightmap[*y as usize][*x as usize])
                            .collect::<Vec<_>>()),
                    )
                })
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
