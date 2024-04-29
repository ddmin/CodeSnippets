use crate::*;

const INPUT: &str = include_str!("../../inputs/day16.txt");

#[derive(Clone)]
struct Transmission(String);

impl Transmission {
    fn bisect(&mut self, idx: usize) -> Transmission {
        let (left, right) = self.0.split_at(idx);
        let left = left.to_string();
        *self = Transmission(right.to_string());

        Transmission(left)
    }
}

impl fmt::Debug for Transmission {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        fmt::Debug::fmt(&self.0, f)
    }
}

impl Deref for Transmission {
    type Target = String;
    fn deref(&self) -> &Self::Target {
        &self.0
    }
}

impl FromStr for Transmission {
    type Err = ();
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        Ok(Transmission(s.to_string()))
    }
}

#[derive(Debug, Clone)]
enum Packet {
    Literal {
        version: String,
        value: usize,
        tail: Transmission,
    },
    Operator {
        version: String,
        type_id: String,
        subsections: Vec<Packet>,
        tail: Transmission,
    },
}

impl Packet {
    fn version_sum(&self) -> usize {
        match self {
            Packet::Literal { version, .. } => usize::from_str_radix(version, 2).unwrap(),
            Packet::Operator {
                version,
                subsections,
                ..
            } => {
                usize::from_str_radix(version, 2).unwrap()
                    + subsections
                        .iter()
                        .map(|subsection| subsection.version_sum())
                        .sum::<usize>()
            }
        }
    }
}

impl FromStr for Packet {
    type Err = ();
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let mut transmission = Transmission::from_str(s).unwrap();

        let version = transmission.bisect(3);
        let type_id = transmission.bisect(3);

        match type_id.as_str() {
            "100" => {
                let mut value = 0;
                let mut bits_counter = 0;
                loop {
                    let group = transmission.bisect(5);
                    let (bit, val) = group.split_at(1);

                    value += usize::from_str_radix(val, 2).unwrap();
                    bits_counter += 5;
                    if bit.chars().nth(0).unwrap() == '0' {
                        break;
                    }
                }
                transmission = transmission.bisect(bits_counter % 4);
                Ok(Packet::Literal {
                    version: version.to_string(),
                    value,
                    tail: transmission,
                })
            }
            type_id => {
                let length_type_id = transmission.bisect(1);

                match length_type_id.as_str() {
                    "0" => {
                        let length = usize::from_str_radix(&transmission.bisect(15), 2).unwrap();
                        transmission = transmission.bisect(length);

                        let mut subsections = Vec::new();
                        while transmission.len() > 6 {
                            let subsection = Packet::from_str(&transmission).unwrap();
                            match subsection {
                                Packet::Literal { ref tail, .. } => {
                                    subsections.push(subsection.clone());
                                    transmission = tail.clone();
                                    if transmission.len() < 6 {
                                        break;
                                    }
                                }
                                Packet::Operator { ref tail, .. } => {
                                    subsections.push(subsection.clone());
                                    transmission = tail.clone();
                                    if transmission.len() < 6 {
                                        break;
                                    }
                                }
                            }
                        }

                        Ok(Packet::Operator {
                            version: version.to_string(),
                            type_id: type_id.to_string(),
                            tail: transmission,
                            subsections,
                        })
                    }
                    "1" => {
                        let number = usize::from_str_radix(&transmission.bisect(11), 2).unwrap();

                        let mut subsections = Vec::new();
                        for _ in 0..number {
                            let subsection = Packet::from_str(&transmission).unwrap();
                            match subsection {
                                Packet::Literal { ref tail, .. } => {
                                    subsections.push(subsection.clone());
                                    transmission = tail.clone();
                                    if transmission.len() < 6 {
                                        break;
                                    }
                                }
                                Packet::Operator { ref tail, .. } => {
                                    subsections.push(subsection.clone());
                                    transmission = tail.clone();
                                    if transmission.len() < 6 {
                                        break;
                                    }
                                }
                            }
                        }
                        Ok(Packet::Operator {
                            version: version.to_string(),
                            type_id: type_id.to_string(),
                            tail: transmission,
                            subsections,
                        })
                    }
                    _ => unreachable!(),
                }
            }
        }
    }
}

pub fn part1(input: &str) -> i32 {
    let binary = input
        .chars()
        .map(|c| format!("{:04b}", c.to_digit(16).unwrap()))
        .collect::<String>();

    let packet = Packet::from_str(&binary).unwrap();
    println!("{:?}", input);
    println!("{:?}", binary);
    println!("{:?}", packet);
    packet.version_sum() as i32
}

#[allow(unused)]
pub fn part2(input: &str) -> i32 {
    0
}

pub fn run() {
    println!("Part 1: {}", part1(INPUT));
    println!("Part 2: {}", part2(INPUT));
}

#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE_1: &str = include_str!("../../examples/day16.txt");
    const EXAMPLE_2: &str = "38006F45291200";
    const EXAMPLE_3: &str = "EE00D40C823060";
    const EXAMPLE_4: &str = "8A004A801A8002F478";
    const EXAMPLE_5: &str = "620080001611562C8802118E34";
    const EXAMPLE_6: &str = "C0015000016115A2E0802F182340";
    const EXAMPLE_7: &str = "A0016C880162017C3686B18A3D4780";

    #[test]
    fn example1_1() {
        assert_eq!(part1(EXAMPLE_1), 6);
    }

    #[test]
    fn example1_2() {
        assert_eq!(part1(EXAMPLE_2), 1);
    }

    #[test]
    fn example1_3() {
        assert_eq!(part1(EXAMPLE_3), 7);
    }

    #[test]
    fn example1_4() {
        assert_eq!(part1(EXAMPLE_4), 16);
    }

    #[test]
    fn example1_5() {
        assert_eq!(part1(EXAMPLE_5), 12);
    }

    #[test]
    fn example1_6() {
        assert_eq!(part1(EXAMPLE_6), 23);
    }

    #[test]
    fn example1_7() {
        assert_eq!(part1(EXAMPLE_7), 31);
    }

    #[test]
    fn example2() {
        assert_eq!(part2(EXAMPLE_1), 0);
    }
}
