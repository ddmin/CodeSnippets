use std::fmt;

pub struct Hero {
    name: String,
    class: Class,
    stats: Stats,
}

impl Hero {
    pub fn new(name: String, class: Class) -> Hero {
        let stats = Class::gen_stats(&class);
        Hero { name, class, stats }
    }
}

impl fmt::Display for Hero {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", self.name)
    }
}

pub enum Class {
    Archer,
    Assassin,
    Priest,
    Warrior,
    Wizard,
}

impl Class {
    fn gen_stats(class: &Class) -> Stats {
        match class {
            Class::Archer => Stats {
                atk: 1,
                def: 1,
                spd: 1,
                crit_rate: 0.5,
                crit_dmg: 0.5,
            },
            Class::Assassin => Stats {
                atk: 1,
                def: 1,
                spd: 1,
                crit_rate: 0.5,
                crit_dmg: 0.5,
            },
            Class::Priest => Stats {
                atk: 1,
                def: 1,
                spd: 1,
                crit_rate: 0.5,
                crit_dmg: 0.5,
            },
            Class::Warrior => Stats {
                atk: 1,
                def: 1,
                spd: 1,
                crit_rate: 0.5,
                crit_dmg: 0.5,
            },
            Class::Wizard => Stats {
                atk: 1,
                def: 1,
                spd: 1,
                crit_rate: 0.5,
                crit_dmg: 0.5,
            },
        }
    }
}

pub struct Stats {
    atk: i32,
    def: i32,
    spd: i32,
    crit_rate: f32,
    crit_dmg: f32,
}
