use crate::*;

const INPUT: &str = include_str!("../../inputs/day13.txt");

#[derive(Clone)]
enum Mark {
    Marked,
    Unmarked,
}

impl fmt::Debug for Mark {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            Mark::Marked => write!(f, "#"),
            Mark::Unmarked => write!(f, "."),
        }
    }
}

struct Paper {
    paper: Vec<Vec<Mark>>,
    width: usize,
    height: usize,
}

type Coordinate = (usize, usize);

impl Paper {
    fn new(dots: Vec<Coordinate>) -> Paper {
        let (mut width, mut height) = (0, 0);
        dots.iter().for_each(|(x, y)| {
            width = width.max(*x);
            height = height.max(*y);
        });

        let mut paper = vec![vec![Mark::Unmarked; width + 1]; height + 1];
        dots.iter().for_each(|(x, y)| paper[*y][*x] = Mark::Marked);

        Paper {
            paper,
            width,
            height,
        }
    }
}

impl fmt::Debug for Paper {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        for row in self.paper.iter() {
            for mark in row.iter() {
                write!(f, "{:?}", mark)?;
            }
            writeln!(f)?;
        }
        write!(f, "")
    }
}

#[derive(Debug)]
enum Fold {
    Vertical(usize),
    Horizontal(usize),
}

fn parse_input(input: &str) -> (Paper, Vec<Fold>) {
    let mut input = input.split("\n\n");

    let dots = bifurcate(input.next().unwrap(), ",")
        .into_iter()
        .map(|(a, b)| (a.parse::<usize>().unwrap(), b.parse::<usize>().unwrap()))
        .collect::<Vec<_>>();

    let folds = bifurcate(input.next().unwrap(), "=")
        .into_iter()
        .map(|(axis, num)| match axis {
            "fold along x" => Fold::Horizontal(num.parse().unwrap()),
            "fold along y" => Fold::Vertical(num.parse().unwrap()),
            _ => unreachable!(),
        })
        .collect::<Vec<_>>();

    (Paper::new(dots), folds)
}

pub fn part1(input: &str) -> i32 {
    let (paper, folds) = parse_input(input);
    println!("{:?}", paper);
    println!("{:?}", folds);
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
    const EXAMPLE: &str = include_str!("../../examples/day13.txt");

    #[test]
    fn example1() {
        assert_eq!(part1(EXAMPLE), 17);
    }

    #[test]
    fn example2() {
        assert_eq!(part2(EXAMPLE), 0);
    }
}
