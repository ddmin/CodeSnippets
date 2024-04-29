fn parse_input(input: &str) -> Vec<&str> {
    input.lines().collect()
}

fn mirror(c: char) -> char {
    let mut characters = vec!['(', '[', '{', '<', ')', ']', '}', '>'];
    let idx = characters.iter().position(|&x| c == x).unwrap();
    characters.rotate_right(4);
    characters[idx]
}

const INPUT: &str = include_str!("../../inputs/day10.txt");

pub fn part1(input: &str) -> i32 {
    let mut score = 0;
    for chunk in parse_input(input) {
        let mut stack = Vec::new();
        for c in chunk.chars() {
            match c {
                '(' | '[' | '{' | '<' => stack.push(c),
                ')' | ']' | '}' | '>' => {
                    let top = stack.pop().unwrap();
                    if mirror(top) != c {
                        score += match c {
                            ')' => 3,
                            ']' => 57,
                            '}' => 1197,
                            '>' => 25137,
                            _ => unreachable!(),
                        };
                        break;
                    }
                }
                _ => unreachable!(),
            }
        }
    }
    score
}

pub fn part2(input: &str) -> i64 {
    let mut scores = parse_input(input)
        .into_iter()
        .map(|chunk| {
            let mut stack = Vec::new();

            for c in chunk.chars() {
                match c {
                    '(' | '[' | '{' | '<' => stack.push(c),
                    ')' | ']' | '}' | '>' => {
                        let top = stack.pop().unwrap();
                        if mirror(top) != c {
                            return -1;
                        }
                    }
                    _ => unreachable!(),
                }
            }
            stack
                .iter()
                .rev()
                .map(|&c| mirror(c))
                .map(|c| {
                    [')', ']', '}', '>']
                        .into_iter()
                        .position(|x| c == x)
                        .unwrap()
                        + 1
                })
                .fold(0, |acc, point| 5 * acc + point as i64)
        })
        .filter(|&score| score >= 0)
        .collect::<Vec<_>>();

    scores.sort_unstable();

    scores[scores.len() / 2] as i64
}

pub fn run() {
    println!("Part 1: {}", part1(INPUT));
    println!("Part 2: {}", part2(INPUT));
}

#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE: &str = include_str!("../../examples/day10.txt");

    #[test]
    fn example1() {
        assert_eq!(part1(EXAMPLE), 26397);
    }

    #[test]
    fn example2() {
        assert_eq!(part2(EXAMPLE), 288957);
    }
}
