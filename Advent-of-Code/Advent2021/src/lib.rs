pub mod days;
pub use std::fmt;
pub use std::fs;

#[allow(unused)]
pub fn bifurcate<'a>(input: &'a str, split: &str) -> Vec<(&'a str, &'a str)> {
    input
        .lines()
        .map(|line| line.split_once(split).unwrap())
        .collect()
}

#[allow(unused)]
fn split(input: &str, delimiter: &str) -> Vec<i32> {
    input.split(delimiter).map(|n| n.parse().unwrap()).collect()
}

#[allow(unused)]
fn lines_to_i32(input: &str) -> Vec<i32> {
    input.lines().map(|n| n.parse().unwrap()).collect()
}

pub fn run_days(days: Vec<usize>) {
    for day in days {
        println!("Day {}", day);
        match day {
            1 => days::day01::run(),
            2 => days::day02::run(),
            3 => days::day03::run(),
            4 => days::day04::run(),
            5 => days::day05::run(),
            6 => days::day06::run(),
            7 => days::day07::run(),
            8 => days::day08::run(),
            9 => days::day09::run(),
            10 => days::day10::run(),
            11 => days::day11::run(),
            12 => days::day12::run(),
            13 => days::day13::run(),
            14 => days::day14::run(),
            15 => days::day15::run(),
            16 => days::day16::run(),
            17 => days::day17::run(),
            18 => days::day18::run(),
            19 => days::day19::run(),
            20 => days::day20::run(),
            21 => days::day21::run(),
            22 => days::day22::run(),
            23 => days::day23::run(),
            24 => days::day24::run(),
            25 => days::day25::run(),
            _ => (),
        }
        println!();
    }
}
