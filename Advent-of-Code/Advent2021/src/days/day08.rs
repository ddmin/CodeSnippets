use crate::*;
use std::collections::HashMap;

const INPUT: &str = include_str!("../../inputs/day08.txt");

//  0000
// 1    2
// 1    2
//  3333
// 4    5
// 4    5
//  6666

#[allow(unused)]
struct SegmentDisplay(HashMap<i32, Vec<i32>>);

#[allow(unused)]
impl SegmentDisplay {
    fn new() -> SegmentDisplay {
        let mut segments: HashMap<i32, Vec<i32>> = HashMap::new();
        //                      0  1  2  3  4  5  6
        segments.insert(0, vec![1, 1, 1, 0, 1, 1, 1]);
        segments.insert(1, vec![0, 0, 1, 0, 0, 1, 0]);
        segments.insert(2, vec![1, 0, 1, 1, 1, 0, 1]);
        segments.insert(3, vec![1, 0, 1, 1, 0, 1, 1]);
        segments.insert(4, vec![0, 1, 1, 1, 0, 1, 0]);
        segments.insert(5, vec![1, 1, 0, 1, 0, 1, 1]);
        segments.insert(6, vec![1, 1, 0, 1, 1, 1, 1]);
        segments.insert(7, vec![1, 0, 1, 0, 0, 1, 0]);
        segments.insert(8, vec![1, 1, 1, 1, 1, 1, 1]);
        segments.insert(9, vec![1, 1, 1, 1, 0, 1, 1]);

        SegmentDisplay(segments)
    }

    fn display(&self, n: usize) {
        assert!(n < 10);
        let segments = self.0.get(&(n as i32)).unwrap();

        let single = "•".to_string();
        let quad = "••••".to_string();

        let mut zero = "    ";
        let mut one = " ";
        let mut two = " ";
        let mut three = "    ";
        let mut four = " ";
        let mut five = " ";
        let mut six = "    ";

        if segments[0] == 1 {
            zero = &quad;
        };

        if segments[1] == 1 {
            one = &single;
        };

        if segments[2] == 1 {
            two = &single;
        };

        if segments[3] == 1 {
            three = &quad;
        };

        if segments[4] == 1 {
            four = &single;
        };

        if segments[5] == 1 {
            five = &single;
        };

        if segments[6] == 1 {
            six = &quad;
        };

        println!(
            " {0} \n{1}    {2}\n{1}    {2}\n {3} \n{4}    {5}\n{4}    {5}\n {6} ",
            zero, one, two, three, four, five, six
        );
    }
}

fn shared_chars(first: &str, second: &str) -> i32 {
    first
        .chars()
        .filter(|&c| second.chars().any(|target| c == target))
        .count() as i32
}

fn decode(length: usize, shared_one: i32, shared_four: i32) -> i32 {
    match (length, shared_one, shared_four) {
        (2, _, _) => 1,
        (3, _, _) => 7,
        (4, _, _) => 4,
        (7, _, _) => 8,
        (5, 1, 2) => 2,
        (5, 1, 3) => 5,
        (5, 2, 3) => 3,
        (6, 1, 3) => 6,
        (6, 2, 3) => 0,
        (6, 2, 4) => 9,
        _ => unreachable!(),
    }
}

pub fn part1(input: &str) -> i32 {
    // Four numbers have unique signal lengths
    //                                    1  4  7  8
    const UNIQUE_SIGNALS: &[usize; 4] = &[2, 4, 3, 7];
    let input = bifurcate(input, " | ");
    input
        .iter()
        .map(|(_, out)| out)
        .flat_map(|signals| signals.split_ascii_whitespace().collect::<Vec<_>>())
        .filter(|signal| UNIQUE_SIGNALS.contains(&signal.len()))
        .count() as i32
}

pub fn part2(input: &str) -> i32 {
    let input = bifurcate(input, " | ");

    let inputs = input
        .iter()
        .map(|(input, _)| input)
        .map(|signals| signals.split_ascii_whitespace().collect::<Vec<_>>());

    let outputs = input
        .iter()
        .map(|(_, output)| output)
        .map(|signals| signals.split_ascii_whitespace().collect::<Vec<_>>());

    inputs.zip(outputs).map(|(input, output)| {
        let one = input.iter().find(|signal| signal.len() == 2).unwrap();
        let four = input.iter().find(|signal| signal.len() == 4).unwrap();

        output
            .iter()
            .map(|signal| {
                decode(
                    signal.len(),
                    shared_chars(one, signal),
                    shared_chars(four, signal),
                )
            })
            .rev()
            .enumerate()
            .fold(0, |sum, (idx, n)| sum + n * 10i32.pow(idx as u32))
    }).sum()
}

pub fn run() {
    println!("Part 1: {}", part1(INPUT));
    println!("Part 2: {}", part2(INPUT));
}

#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE: &str = include_str!("../../examples/day08.txt");

    #[test]
    fn example1() {
        assert_eq!(part1(EXAMPLE), 26);
    }

    #[test]
    fn example2() {
        assert_eq!(part2(EXAMPLE), 61229);
    }
}
