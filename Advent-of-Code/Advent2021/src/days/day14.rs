use crate::*;
use std::collections::HashMap;

const INPUT: &str = include_str!("../../inputs/day14.txt");

type PairInsertions = HashMap<(char, char), char>;

fn parse_input(input: &str) -> (&str, PairInsertions) {
    let mut input = input.split("\n\n");

    let polymer = input.next().unwrap();

    let insertion_rules = bifurcate(input.next().unwrap(), " -> ");
    let insertion_rules = insertion_rules
        .iter()
        .map(|(pair, _)| {
            let mut chars = pair.chars();
            (chars.next().unwrap(), chars.next().unwrap())
        })
        .zip(
            insertion_rules
                .iter()
                .map(|(_, insert)| insert.chars().next().unwrap()),
        )
        .collect::<PairInsertions>();

    (polymer, insertion_rules)
}

fn polymerize(polymer: &str, insertion_rules: PairInsertions, steps: usize) -> i64 {
    let mut pairs_count = HashMap::new();
    for element in polymer.chars().zip(polymer.chars().skip(1)) {
        *pairs_count.entry(element).or_insert(0) += 1
    }

    for _ in 0..steps {
        let mut next_step = HashMap::new();

        // for each pair of elements, insert a new element in between
        //                       (A, B)
        //                       /    \
        //                   (A, C)  (C, B)
        for (&(a, b), &count) in pairs_count.iter() {
            let c = insertion_rules[&(a, b)];
            *next_step.entry((a, c)).or_insert(0) += count;
            *next_step.entry((c, b)).or_insert(0) += count;
        }
        pairs_count = next_step;
    }

    // count the occurrence of each element
    //     (first item of each tuples)
    //   A    ->   C    ->   B    ->   D
    // (A, C) -> (C, B) -> (B, D) -> (D, E)
    let mut elements_count = HashMap::new();
    for (&(a, _), count) in pairs_count.iter() {
        *elements_count.entry(a).or_insert(0) += count;
    }

    // the final character is not represented,
    // insert last character count manually.
    //   A    ->   C    ->   B    ->   D    ->   E
    // (A, C) -> (C, B) -> (B, D) -> (D, E)    (+1)
    *elements_count
        .entry(polymer.chars().last().unwrap())
        .or_insert(0) += 1;

    let mut counts = elements_count.values().copied().collect::<Vec<_>>();
    counts.sort_unstable();

    counts.iter().last().unwrap() - counts.get(0).unwrap()
}

pub fn part1(input: &str) -> i64 {
    let (polymer, insertion_rules) = parse_input(input);
    polymerize(polymer, insertion_rules, 10)
}

pub fn part2(input: &str) -> i64 {
    let (polymer, insertion_rules) = parse_input(input);
    polymerize(polymer, insertion_rules, 40)
}

pub fn run() {
    println!("Part 1: {}", part1(INPUT));
    println!("Part 2: {}", part2(INPUT));
}

#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE: &str = include_str!("../../examples/day14.txt");

    #[test]
    fn example1() {
        assert_eq!(part1(EXAMPLE), 1588);
    }

    #[test]
    fn example2() {
        assert_eq!(part2(EXAMPLE), 2188189693529);
    }
}
