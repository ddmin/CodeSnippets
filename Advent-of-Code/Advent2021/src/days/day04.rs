use std::fmt;

const INPUT: &str = include_str!("../../inputs/day04.txt");

type Board = Vec<Vec<i32>>;

struct Bingo {
    board: Board,
    called: Vec<(i32, i32)>,
}

impl Bingo {
    fn new(board: Board) -> Bingo {
        Bingo {
            board,
            called: Vec::new(),
        }
    }

    fn check_horizontal(&self) -> bool {
        for col in 0..self.board.len() {
            let mut count = 0;
            for row in 0..self.board[col].len() {
                match self.called.contains(&(col as i32, row as i32)) {
                    true => count += 1,
                    false => break,
                }
            }
            if count == 5 {
                return true;
            }
        }
        false
    }

    fn check_vertical(&self) -> bool {
        for row in 0..self.board[0].len() {
            let mut count = 0;
            for col in 0..self.board.len() {
                match self.called.contains(&(col as i32, row as i32)) {
                    true => count += 1,
                    false => break,
                }
            }
            if count == 5 {
                return true;
            }
        }
        false
    }

    fn check_win(&self) -> bool {
        self.check_horizontal() || self.check_vertical()
    }

    fn call_number(&mut self, number: i32) {
        for col in 0..self.board.len() {
            for row in 0..self.board[col].len() {
                if self.board[col][row] == number {
                    self.called.push((col as i32, row as i32));
                }
            }
        }
    }

    fn sum_unguessed(&self) -> i32 {
        let mut sum = 0;
        for col in 0..self.board.len() {
            for row in 0..self.board[col].len() {
                if !self.called.contains(&(col as i32, row as i32)) {
                    sum += self.board[col][row];
                }
            }
        }
        sum
    }
}

impl fmt::Display for Bingo {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        for col in 0..self.board.len() {
            for row in 0..self.board[col].len() {
                write!(
                    f,
                    "{}{}",
                    match self.called.contains(&(col as i32, row as i32)) {
                        true => " *",
                        false => "  ",
                    },
                    format!("{:02}", self.board[col][row])
                )?;
            }
            if col != self.board.len() {
                writeln!(f)?;
            }
        }
        write!(f, "")
    }
}

fn parse_input(input: &str) -> (Vec<i32>, Vec<Bingo>) {
    let mut input = input.split("\n\n");

    let nums = input
        .next()
        .unwrap()
        .split(',')
        .map(|n| n.parse().unwrap())
        .collect::<Vec<i32>>();

    let boards = input
        .map(|boards| {
            Bingo::new(
                boards
                    .lines()
                    .map(|line| {
                        line.split_ascii_whitespace()
                            .map(|n| n.parse::<i32>().unwrap())
                            .collect::<Vec<_>>()
                    })
                    .collect::<Board>(),
            )
        })
        .collect::<Vec<_>>();

    (nums, boards)
}

pub fn part1(input: &str) -> i32 {
    let (nums, mut boards) = parse_input(input);
    for num in nums.iter() {
        for board in 0..boards.len() {
            boards[board].call_number(*num);
            match boards[board].check_win() {
                true => {
                    println!("\nWinning Board:\n{}", boards[board]);
                    return num * boards[board].sum_unguessed();
                }
                false => continue,
            }
        }
    }
    0
}

pub fn part2(input: &str) -> i32 {
    let (nums, mut boards) = parse_input(input);

    let mut count = boards.len();
    let mut won = Vec::new();

    for num in nums.iter() {
        for board in 0..boards.len() {
            boards[board].call_number(*num);
            match boards[board].check_win() {
                true => {
                    if !won.contains(&board) {
                        count -= 1;
                        won.push(board);
                    }
                    if count == 0 {
                        println!("\nLosing Board:\n{}", boards[board]);
                        return num * boards[board].sum_unguessed();
                    }
                }
                false => continue,
            }
        }
    }
    0
}

pub fn run() {
    println!("{}", part1(INPUT));
    println!("{}", part2(INPUT));
}

#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE: &str = include_str!("../../examples/day04.txt");

    #[test]
    fn example1() {
        assert_eq!(part1(EXAMPLE), 4512);
    }

    #[test]
    fn example2() {
        assert_eq!(part2(EXAMPLE), 1924);
    }
}
