use crate::*;
use std::collections::HashSet;

const INPUT: &str = include_str!("../../inputs/day13.txt");

enum Fold {
    Vertical(usize),
    Horizontal(usize),
}

struct Paper {
    marked: HashSet<Coordinate>,
    width: usize,
    height: usize,
}

type Coordinate = (usize, usize);

impl Paper {
    fn new(marked: HashSet<Coordinate>) -> Paper {
        let (mut width, mut height) = (0, 0);
        marked.iter().for_each(|(x, y)| {
            width = width.max(*x);
            height = height.max(*y);
        });

        Paper {
            marked,
            width,
            height,
        }
    }

    fn fold(&mut self, fold: &Fold) {
        self.marked = match fold {
            Fold::Horizontal(crease) => {
                self.width = *crease;
                self.marked
                    .iter()
                    .map(|&coordinate| match coordinate {
                        (x, y) if x < *crease => (x, y),
                        (x, y) => (crease * 2 - x, y),
                    })
                    .collect::<HashSet<_>>()
            }
            Fold::Vertical(crease) => {
                self.height = *crease;
                self.marked
                    .iter()
                    .map(|&coordinate| match coordinate {
                        (x, y) if y < *crease => (x, y),
                        (x, y) => (x, crease * 2 - y),
                    })
                    .collect::<HashSet<_>>()
            }
        }
    }
}

impl fmt::Debug for Paper {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        for y in 0..self.height {
            for x in 0..self.width {
                if self.marked.contains(&(x, y)) {
                    write!(f, "█")?;
                } else {
                    write!(f, ".")?;
                }
            }
            writeln!(f)?;
        }
        write!(f, "")
    }
}

fn parse_input(input: &str) -> (Paper, Vec<Fold>) {
    let mut input = input.split("\n\n");

    let dots = bifurcate(input.next().unwrap(), ",")
        .into_iter()
        .map(|(a, b)| (a.parse::<usize>().unwrap(), b.parse::<usize>().unwrap()))
        .collect::<HashSet<_>>();

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
    let (mut paper, folds) = parse_input(input);
    paper.fold(&folds[0]);
    paper.marked.len() as i32
}

pub fn part2(input: &str) {
    let (mut paper, folds) = parse_input(input);
    folds.iter().for_each(|fold| paper.fold(fold));
    println!("{:?}", paper);
}

pub fn run() {
    println!("Part 1: {}", part1(INPUT));
    println!("Part 2:");
    part2(INPUT);
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
        part2(EXAMPLE);
    }
}
