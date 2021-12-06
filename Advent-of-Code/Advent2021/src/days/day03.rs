const INPUT: &str = include_str!("../../inputs/day03.txt");

fn max_bit(input: &[i32], pos: usize) -> i32 {
    let mut count = [0, 0];
    for &bit in input.iter() {
        count[bit as usize >> pos & 1] += 1;
    }
    (count[0] <= count[1]) as i32
}

fn vec_to_i32(vec: &[i32]) -> i32 {
    let mut sum = 0;
    for (idx, bit) in vec.iter().rev().enumerate() {
        sum += bit << idx;
    }
    sum
}

pub fn part1(input: &str) -> i32 {
    let lines = input
        .lines()
        .map(|str| i32::from_str_radix(str, 2).unwrap())
        .collect::<Vec<_>>();

    let gamma = (0..input.lines().next().unwrap().len())
        .rev()
        .map(|idx| max_bit(&lines, idx))
        .collect::<Vec<_>>();

    let epsilon = gamma
        .iter()
        .map(|bit| match bit {
            0 => 1,
            1 => 0,
            _ => unreachable!(),
        })
        .collect::<Vec<_>>();

    vec_to_i32(&gamma) * vec_to_i32(&epsilon)
}

pub fn part2(input: &str) -> i32 {
    let lines = input
        .lines()
        .map(|str| i32::from_str_radix(str, 2).unwrap())
        .collect::<Vec<_>>();

    let mut oxygen = lines.clone();
    let mut co2 = lines;

    for idx in (0..input.lines().next().unwrap().len()).rev() {
        let bit = max_bit(&oxygen, idx);
        oxygen.retain(|n| (n >> idx) & 1 == bit);
        if oxygen.len() == 1 {
            break;
        }
    }

    for idx in (0..input.lines().next().unwrap().len()).rev() {
        let bit = max_bit(&co2, idx) ^ 1;
        co2.retain(|n| (n >> idx) & 1 == bit);
        if co2.len() == 1 {
            break;
        }
    }
    vec_to_i32(&oxygen) * vec_to_i32(&co2)
}

pub fn run() {
    println!("{}", part1(INPUT));
    println!("{}", part2(INPUT));
}

#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE: &str = include_str!("../../examples/day03.txt");

    #[test]
    fn example1() {
        assert_eq!(part1(EXAMPLE), 198);
    }

    #[test]
    fn example2() {
        assert_eq!(part2(EXAMPLE), 230);
    }
}
