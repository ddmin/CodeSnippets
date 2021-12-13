use crate::*;

const INPUT: &str = include_str!("../../inputs/day13.txt");

#[derive(Debug)]
enum Fold {
    Vertical(usize),
    Horizontal(usize),
}

#[derive(Clone)]
enum Mark {
    Marked,
    Unmarked,
}

impl Mark {
    fn is_marked(&self) -> bool {
        match self {
            Mark::Marked => true,
            Mark::Unmarked => false,
        }
    }
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

        Paper { paper }
    }

    fn fold(&mut self, folds: &[Fold]) {
        for fold in folds {
            match fold {
                Fold::Horizontal(crease) => {
                    for col in 0..self.paper.len() {
                        for row in 0..self.paper[col].len() {
                            // if self.paper[col][self.paper[col].len() - row - 1].is_marked() {
                            //     self.paper[col][row] = Mark::Marked;
                            // }
                            if self.paper[col][self.paper[col].len() - row - 1].is_marked() {
                                self.paper[col][row] = Mark::Marked;
                            }
                        }
                    }
                    self.paper = self
                        .paper
                        .iter()
                        .map(|row| {
                            row.iter()
                                .enumerate()
                                .filter(|(idx, _)| idx > crease)
                                .map(|(_, mark)| mark.clone())
                                .collect::<Vec<_>>()
                        })
                        .collect::<Vec<_>>()
                }
                Fold::Vertical(crease) => {
                    for col in 0..=*crease {
                        for row in 0..self.paper[col].len() {
                            if self.paper[self.paper.len() - col - 1][row].is_marked() {
                                self.paper[col][row] = Mark::Marked;
                            }
                        }
                    }
                    let (top, _bottom) = self.paper.split_at(*crease);
                    self.paper = top.to_vec();
                }
            }
        }
    }

    fn count_marked(&self) -> i32 {
        self.paper
            .iter()
            .map(|row| row.iter().filter(|mark| mark.is_marked()))
            .flatten()
            .count() as i32
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
    let (mut paper, folds) = parse_input(input);

    // Part 1: only fold once
    let (first, _) = folds.split_at(1);

    paper.fold(first);
    paper.count_marked()
}

pub fn part2(input: &str) {
    let (mut paper, folds) = parse_input(input);
    paper.fold(&folds);
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
