use crate::*;

pub fn part1(input: &str) {
    let input = lines_to_i32(input);
    let (base_iter, mut cmp_iter) = (input.iter(), input.iter());

    cmp_iter.next();

    // base: 0 1 2 3 4 ...
    // cmp : 1 2 3 4 5 ...
    let solution = base_iter
        .zip(cmp_iter)
        .map(|(&base, &cmp)| base < cmp)
        .filter(|&bool| bool)
        .count();

    println!("Part 1: {}", solution);
}

pub fn part2(input: &str) {
    let input = lines_to_i32(input);
    let (base_iter, cmp_iter) = (input.iter(), input.iter().skip(3));

    // A
    // A   B   <-- Equal
    // A   B   <-- Equal
    //     B
    let solution = base_iter
        .zip(cmp_iter)
        .map(|(&base, &cmp)| base < cmp)
        .filter(|&bool| bool)
        .count();

    println!("Part 2: {}", solution);
}

pub fn run() {
    let input: String = read_input("inputs/day01.txt");
    part1(&input);
    part2(&input);
}
