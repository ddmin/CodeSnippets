use advent_of_code_2020 as aoc;
use std::fs;

fn main() {
    // day1();
    day2();
}

fn day2() {
    let input = fs::read_to_string("2.txt").expect("Failed to read file.");
    aoc::day2::part1(&input);
}

#[allow(dead_code)]
fn day1() {
    let input = fs::read_to_string("1.txt").expect("Failed to read file.");
    aoc::day1::part1(&input);
    aoc::day1::part2(&input);
}
