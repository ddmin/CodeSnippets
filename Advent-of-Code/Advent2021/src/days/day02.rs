use crate::*;

const INPUT: &str = include_str!("../../inputs/day02.txt");

pub fn part1(input: &str) -> i32 {
    let commands = bifurcate(input, " ");
    let commands = commands
        .iter()
        .map(|(cmd, amt)| (cmd, amt.parse::<i32>().unwrap()))
        .collect::<Vec<_>>();

    let (horizontal, vertical) =
        commands
            .iter()
            .fold((0, 0), |(horizontal, depth), (&cmd, amt)| match cmd {
                "forward" => (horizontal + amt, depth),
                "up" => (horizontal, depth - amt),
                "down" => (horizontal, depth + amt),
                _ => unreachable!(),
            });
    horizontal * vertical
}

pub fn part2(input: &str) -> i32 {
    let commands = bifurcate(input, " ");
    let commands = commands
        .iter()
        .map(|(command, amt)| (command, amt.parse::<i32>().unwrap()))
        .collect::<Vec<_>>();

    let (horizontal, vertical, _) = commands.iter().fold(
        (0, 0, 0),
        |(horizontal, depth, aim), (&cmd, amt)| match cmd {
            "forward" => (horizontal + amt, depth + aim * amt, aim),
            "up" => (horizontal, depth, aim - amt),
            "down" => (horizontal, depth, aim + amt),
            _ => unreachable!(),
        },
    );

    horizontal * vertical
}

pub fn run() {
    println!("Part 1: {}", part1(INPUT));
    println!("Part 2: {}", part2(INPUT));
}

#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE: &str = include_str!("../../examples/day02.txt");

    #[test]
    fn example1() {
        assert_eq!(part1(EXAMPLE), 150);
    }

    #[test]
    fn example2() {
        assert_eq!(part2(EXAMPLE), 900);
    }
}
