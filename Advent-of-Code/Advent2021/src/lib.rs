pub mod days;
pub use colored::*;
pub use std::fmt;
pub use std::fs;
pub use std::str::FromStr;
pub use std::ops::Deref;

#[allow(unused)]
pub fn bifurcate<'a>(input: &'a str, split: &str) -> Vec<(&'a str, &'a str)> {
    input
        .lines()
        .map(|line| line.split_once(split).unwrap())
        .collect()
}

#[allow(unused)]
fn split<T>(input: &str, delimiter: &str) -> Vec<T>
where
    T: FromStr,
    T::Err: fmt::Debug,
{
    input
        .split(delimiter)
        .map(|n| n.parse::<T>().unwrap())
        .collect()
}

pub fn run_days(days: Vec<usize>) {
    for day in days {
        let now = std::time::Instant::now();
        println!("{}", format!("🎄 Day {} 🎄", day).green());
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
            _ => (),
        }
        let time = now.elapsed().as_millis();
        println!("{}", format!("Time: {}ms", time).yellow());
        println!();
    }
}
