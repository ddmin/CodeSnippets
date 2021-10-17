use std::fmt;

pub enum AbilityClass {
    Attack,
    Heal,
    Buff(usize),
}

impl fmt::Display for AbilityClass {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let stats = ["ATK".to_string(), "DEF".to_string(), "SPD".to_string()];

        let ability = match self {
            AbilityClass::Attack => "ATK".to_string(),
            AbilityClass::Heal => "HEAL".to_string(),
            AbilityClass::Buff(s) => format!("{}+", stats[*s]),
        };

        write!(f, "{}", ability)
    }
}

pub struct Ability {
    name: String,
    class: AbilityClass,
    amt: i32,
}

impl Ability {
    pub fn new(name: String, class: AbilityClass, amt: i32) -> Ability {
        Ability { name, class, amt }
    }
}

impl fmt::Display for Ability {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let spacing = match self.class {
            AbilityClass::Attack => " ",
            _ => "",
        };

        write!(f, "[{}]{} {}: {}", self.class, spacing, self.name, self.amt)
    }
}
