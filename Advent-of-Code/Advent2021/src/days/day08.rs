use crate::*;
use std::collections::{HashMap, HashSet};

const INPUT: &str = include_str!("../../inputs/day08.txt");

struct SegmentDisplay(HashMap<i32, Vec<i32>>);

//  0000
// 1    2
// 1    2
//  3333
// 4    5
// 4    5
//  6666

// 1 ^ 7 => [0                  ]
// 1 ^ 4 => [   1,    3         ]
// 0 ^ 8 => [         3         ]
// 0 ^ 6 => [      2, 3         ]
// 0 ^ 9 => [         3, 4      ]
// 2 ^ 3 => [            4, 5   ]
// 3 ^ 5 => [   1, 2            ]
// 4 ^ 8 => [0,          4,    6]

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

        let mut zero = "    ".to_string();
        let mut one = " ".to_string();
        let mut two = " ".to_string();
        let mut three = "    ".to_string();
        let mut four = " ".to_string();
        let mut five = " ".to_string();
        let mut six = "    ".to_string();

        if segments[0] == 1 {
            zero = "••••".to_string();
        };

        if segments[1] == 1 {
            one = "•".to_string();
        };

        if segments[2] == 1 {
            two = "•".to_string();
        };

        if segments[3] == 1 {
            three = "••••".to_string();
        };

        if segments[4] == 1 {
            four = "•".to_string();
        };

        if segments[5] == 1 {
            five = "•".to_string();
        };

        if segments[6] == 1 {
            six = "••••".to_string();
        };

        println!(
            " {0} \n{1}    {2}\n{1}    {2}\n {3} \n{4}    {5}\n{4}    {5}\n {6} ",
            zero, one, two, three, four, five, six
        );
    }

    fn get(&self, n: usize) -> &Vec<i32> {
        assert!(n < 10);
        self.0.get(&(n as i32)).unwrap()
    }
}

fn character_xor(first: &str, second: &str) -> Vec<char> {
    let mut difference = Vec::new();
    difference.append(
        &mut first
            .chars()
            .filter(|c| !second.chars().collect::<Vec<_>>().contains(c))
            .collect::<Vec<_>>(),
    );

    difference.append(
        &mut second
            .chars()
            .filter(|c| !first.chars().collect::<Vec<_>>().contains(c))
            .collect::<Vec<_>>(),
    );
    difference
}

fn character_and(first: &str, second: &str) -> Vec<char> {
    let mut and = Vec::new();
    and.append(
        &mut first
            .chars()
            .filter(|c| !second.chars().collect::<Vec<_>>().contains(c))
            .collect::<Vec<_>>(),
    );

    and
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
    // Four numbers have unique signal lengths
    //                                    1  4  7  8
    const UNIQUE_SIGNALS: &[usize; 4] = &[2, 4, 3, 7];

    const FIVE_SIGNALS: &[usize; 3] = &[2, 3, 5];
    const SIX_SIGNALS: &[usize; 3] = &[0, 6, 9];

    let segments = SegmentDisplay::new();
    let mut letters_to_segments: HashMap<char, i32> = HashMap::new();
    let input = bifurcate(input, " | ");

    let inputs = input
        .iter()
        .map(|(input, _)| input)
        .map(|signals| signals.split_ascii_whitespace().collect::<Vec<_>>())
        .collect::<Vec<_>>();

    let outputs = input
        .iter()
        .map(|(_, output)| output)
        .map(|signals| signals.split_ascii_whitespace().collect::<Vec<_>>())
        .collect::<Vec<_>>();

    println!("{:?}", inputs);
    println!();

    let first = inputs.get(0).unwrap();

    let fives = first
        .iter()
        .filter(|signal| signal.len() == 5)
        .collect::<Vec<_>>();

    let sixes = first
        .iter()
        .filter(|signal| signal.len() == 6)
        .collect::<Vec<_>>();

    let unique = UNIQUE_SIGNALS
        .iter()
        .map(|&length| {
            first
                .iter()
                .filter(|signal| signal.len() == length)
                .next()
                .unwrap()
        })
        .collect::<Vec<_>>();

    println!("{:?}", first);
    println!("FIVE: {:?}", fives);
    println!("SIX: {:?}", sixes);
    println!("UNIQ: {:?}", unique);
    println!("IDX: {:?}", UNIQUE_SIGNALS);

    // compare 1 and 7 => segment 0
    letters_to_segments.insert(character_xor(unique[0], unique[2])[0], 0);

    letters_to_segments.insert(character_and(unique[0], unique[2])[0], 0);
    0
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
