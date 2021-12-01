use crate::*;

pub fn part1(input: &str) {
    let input = lines_to_i32(input);
    let (mut base_iter, cmp_iter) = (input.iter(), input.iter());

    base_iter.next();

    // base: 1 2 3 4 5 ...
    // cmp : 0 1 2 3 4 ...
    let solution = base_iter
        .zip(cmp_iter)
        .map(|(&base, &cmp)| base > cmp)
        .filter(|&bool| bool)
        .count();

    println!("Part 1: {}", solution);
}

pub fn part2(input: &str) {
    let input = lines_to_i32(input);
    let mut triplets: Vec<i32> = Vec::new();
    for i in 0..input.len() - 2 {
        triplets.push(input[i..i + 3].iter().sum());
    }

    let (mut base_iter, cmp_iter) = (triplets.iter(), triplets.iter());

    base_iter.next();

    // base: 1 2 3 4 5 ...
    // cmp : 0 1 2 3 4 ...
    let solution = base_iter
        .zip(cmp_iter)
        .map(|(&base, &cmp)| base > cmp)
        .filter(|&bool| bool)
        .count();

    println!("Part 2: {}", solution);
}

pub fn run() {
    let input: String = read_input("inputs/day01.txt");
    part1(&input);
    part2(&input);
}
