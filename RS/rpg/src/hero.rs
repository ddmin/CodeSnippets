pub struct Hero {
    name: String,
    class: Class,
    stats: Stats,
}

pub enum Class {
    Archer,
    Assassin,
    Priest,
    Warrior,
    Wizard,
}

pub struct Stats {
    atk: i32,
    def: i32,
    spd: i32,
    crit_rate: i32,
    crit_dmg: i32,
}
