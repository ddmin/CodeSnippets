const INPUT: &str = include_str!("../../inputs/day01.txt");

fn parse_input(input: &str) -> Vec<i32> {
    input.lines().map(|n| n.parse().unwrap()).collect()
}

pub fn part1(input: &str) -> i32 {
    let input = parse_input(input);
    let (base_iter, cmp_iter) = (input.iter(), input.iter().skip(1));

    // base: 0 1 2 3 4 ...
    // cmp : 1 2 3 4 5 ...
    let solution = base_iter
        .zip(cmp_iter)
        .map(|(&base, &cmp)| base < cmp)
        .filter(|&bool| bool)
        .count();

    solution as i32
}

pub fn part2(input: &str) -> i32 {
    let input = parse_input(input);
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

    solution as i32
}

pub fn run() {
    println!("Part 1: {}", part1(INPUT));
    println!("Part 2: {}", part2(INPUT));
}

#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE: &str = include_str!("../../examples/day01.txt");

    #[test]
    fn example1() {
        assert_eq!(part1(EXAMPLE), 7);
    }

    #[test]
    fn example2() {
        assert_eq!(part2(EXAMPLE), 5);
    }
}
